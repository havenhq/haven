import * as fs from "fs/promises";
import {Cloud, CloudStatus} from "../api/pb/manager_pb";
import {CloudInterface} from "./interface";
import {GoogleCloud} from "./gcp/gcp";

class CloudManager {
	gcp: GoogleCloud | null = null;
	aws: CloudInterface | null = null;

	/**
	 * @returns The status of all clouds
	 */
	public async getCloudStatus(): Promise<CloudStatus[]> {
		const res: CloudStatus[] = [];

		res.push(
			new CloudStatus({
				cloud: Cloud.GCP,
				enabled: (await this.gcp?.isAvailable()) ?? false,
			}),
		);

		res.push(
			new CloudStatus({
				cloud: Cloud.AWS,
				enabled: (await this.aws?.isAvailable()) ?? false,
			}),
		);

		return res;
	}

	/**
	 * Creates or updates the GCP key file.
	 *
	 * @param file The key file as a string
	 */
	private async updateGcp(file: string) {
		const isValidJson = await Promise.resolve()
			.then(() => JSON.parse(file))
			.catch(() => false);

		if (isValidJson === false) {
			throw new Error("[updateGcp] Invalid key file");
		}

		// Check if there is already a key file
		const doesKeyExist = await fs
			.access("./credentials/gcp.json")
			.then(() => true)
			.catch(() => false);

		if (doesKeyExist) {
			console.log("[updateGcp] Key file already exists. Deleting old key file.");
			await fs.unlink("./credentials/gcp.json");
		}

		await fs.writeFile("./credentials/gcp.json", file);

		process.env.GOOGLE_APPLICATION_CREDENTIALS = "./credentials/gcp.json";
		this.gcp = new GoogleCloud(isValidJson.project_id, isValidJson.client_email, isValidJson.client_id);
	}

	/**
	 * Creates or updates the AWS key file.
	 *
	 * @param file The key file as a string
	 */
	private async updateAws(file: string) {
		// Check if there is already a key file
		const doesKeyExist = await fs
			.access("./credentials/aws.txt")
			.then(() => true)
			.catch(() => false);

		if (doesKeyExist) {
			console.log("[updateAws] Key file already exists. Deleting old key file.");
			await fs.unlink("./credentials/aws.txt");
		}

		// TODO: we're just trusting the file here, should be validated
		await fs.writeFile("./credentials/aws.txt", file);
	}

	/**
	 * Update credentials of the specified cloud provider.
	 * @param cloud	The cloud provider
	 * @param file The key file as a string
	 */
	public async updateCloud(cloud: Cloud, file: string) {
		if (cloud === Cloud.GCP) {
			await this.updateGcp(file);
		}

		if (cloud === Cloud.AWS) {
			await this.updateAws(file);
		}
	}

	/**
	 * Search for a cloud instance by name.
	 */
	public async getCloudByInstanceName(name: string): Promise<Cloud | undefined> {
		// Check GCP
		const gcpInstances = (await this.gcp?.listInstances()) ?? [];
		if (gcpInstances.find((instance) => instance.workerName === name)) {
			return Cloud.GCP;
		}

		// Check AWS
		const awsInstances = (await this.aws?.listInstances()) ?? [];
		if (awsInstances.find((bucket) => bucket.workerName === name)) {
			return Cloud.AWS;
		}

		return undefined;
	}

	/**
	 * Get cloud controller.
	 */
	public get(cloud: Cloud): CloudInterface {
		if (cloud === Cloud.GCP) {
			if (this.gcp === null) {
				throw new Error("[get] GCP not initialized");
			}

			return this.gcp;
		}

		if (cloud === Cloud.AWS) {
			if (this.aws === null) {
				throw new Error("[get] AWS not initialized");
			}

			return this.aws;
		}

		throw new Error("[get] Unknown cloud provider");
	}
}

export const cloudManager = new CloudManager();
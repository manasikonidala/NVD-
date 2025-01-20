from api.utils import sync_cves_in_batches

if __name__ == "__main__":
    # Sync every 1 hour (3600 seconds) with a batch size of 100
    sync_cves_in_batches(batch_size=100, period_seconds=3600)

import psutil

class SystemMonitor:
    @staticmethod
    def get_system_stats():
        try:
            cpu_usage = psutil.cpu_percent(interval=0.5)

            ram_info = psutil.virtual_memory()
            ram_usage = ram_info.percent

            return cpu_usage, ram_usage
        except Exception as e:
            print(" [ - ] Error fetching system stats {e} ")
            return 0, 0
        
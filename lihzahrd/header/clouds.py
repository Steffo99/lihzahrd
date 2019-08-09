class Clouds:
    """Information about... the clouds in the world?"""
    def __init__(self, bg_cloud: int, cloud_number: int, wind_speed: float):
        self.bg_cloud: int = bg_cloud
        self.cloud_number: int = cloud_number
        self.wind_speed: float = wind_speed

    def __repr__(self):
        return f"WorldClouds(bg_cloud={self.bg_cloud}, cloud_number={self.cloud_number}, wind_speed={self.wind_speed})"

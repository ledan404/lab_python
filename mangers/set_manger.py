"""Set Manger"""


class SetManger:
    """Set Manger class"""

    def __init__(self, video_manger):
        self.video_manger = video_manger

    def __len__(self):
        return len(list(iter(self)))

    def __iter__(self):
        for video in self.video_manger:
            for item in video:
                yield item

    def __getitem__(self, index):
        return self.video_manger[index]

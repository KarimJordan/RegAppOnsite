from django.db import models
from event.models import Event
from guest.models import Guest


# Create your models here.
class Raffler(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    num_of_draws = models.IntegerField()
    label = models.CharField(max_length=500)
    num_of_draws_done = models.IntegerField(default=0)
    draw_duration = models.FloatField(default=5.2)
    item_duration = models.FloatField(default=0.1)
    prize_image = models.TextField()
    background_image = models.TextField()
    conditions = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    @staticmethod
    def copy_raffle(data):
        raffle = Raffler(
            event=data['event'],
            title=data['title'],
            num_of_draws=data['num_of_draws'],
            label=data['label'],
            num_of_draws_done=data['num_of_draws_done'],
            draw_duration=data['draw_duration'],
            item_duration=data['item_duration'],
            prize_image=data['prize_image'],
            background_image=data['background_image'],
            conditions=data['conditions']
        )
        raffle.save()


class RafflerSelectionWinner(models.Model):
    raffle = models.ForeignKey(Raffler, on_delete=models.CASCADE)
    filter_type = models.IntegerField()
    guest_info_field = models.CharField(max_length=200)
    data = models.CharField(max_length=200)


class RafflerWinner(models.Model):
    raffle = models.ForeignKey(Raffler, on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)

    def __str__(self):
        return self.raffle.title + ' ' + str(self.guest.id)

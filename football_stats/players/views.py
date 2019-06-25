import csv, io
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.views import generic
from itertools import chain

from .models import Player, League, Team


class IndexView(generic.ListView):
    template_name = 'players/players.html'
    context_object_name = 'players'

    def get_queryset(self):
        return list(chain(Player.objects.all(), Player._meta.get_fields()))


def rate(stats):
    sum = 0.

    sum += float(stats[4]) / float(stats[3]) * 90 / 30
    sum += float(stats[5]) / float(stats[3]) * 90 / 40
    sum += float(stats[6]) / float(stats[3]) * 90 / 2
    sum += float(stats[7]) / float(stats[3]) * 90 / 1
    sum += float(stats[8]) / float(stats[3]) * 90 / 3
    sum += float(stats[9]) / float(stats[3]) * 90 / 1.5
    sum += float(stats[10]) / float(stats[3]) * 90 / 5
    sum -= float(stats[11]) / float(stats[3]) * 90 / 1.2
    sum -= float(stats[12]) / float(stats[3]) * 90 / 0.5
    sum -= float(stats[13]) / float(stats[3]) * 90 / 1.5
    sum += float(stats[14]) / float(stats[3]) * 90 / 0.5
    sum += float(stats[15]) / float(stats[3]) * 90 / 11
    sum += float(stats[16]) / float(stats[3]) * 90 / 4
    sum += float(stats[17]) / float(stats[3]) * 90 / 1
    sum += float(stats[18]) / float(stats[3]) * 90 / 2
    sum += float(stats[19]) / float(stats[3]) * 90 / 1
    sum += float(stats[20]) / float(stats[3]) * 90 / 1
    sum += float(stats[21]) / float(stats[3]) * 90 / 1
    sum += float(stats[22]) / float(stats[3]) * 90 / 2.5
    sum += float(stats[23]) / float(stats[3]) * 90 / 1
    sum += float(stats[24]) / float(stats[3]) * 90 / 2
    sum += float(stats[25]) / float(stats[3]) * 90 / 1
    sum += float(stats[26]) / float(stats[3]) * 90 / 5
    sum += float(stats[27]) / float(stats[3]) * 90 / 0.5
    sum += float(stats[28]) / float(stats[3]) * 90 / 10

    return sum


@permission_required('admin.can_addlog_entry')
def player_upload(request):
    template = 'players/player_upload.html'

    prompt = {
        'order': ''
    }

    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=':', quotechar='|'):
        for i, stat in enumerate(column):
            if i in [0, 1]:
                continue

            column[i] = column[i].replace('Åš', 'Ś')
            column[i] = column[i].replace(',', '.')
            column[i] = column[i].replace('km', '')
            column[i] = column[i].replace('Â\xa0', '')
            column[i] = column[i].replace('-', '0')
        if int(column[3]) < 180:
            continue
        if column[32] == '0':
            continue
        if not League.objects.filter(name=column[32]):
            League.objects.update_or_create(
                name=column[32]
            )
        if not Team.objects.filter(name=column[31]):
            Team.objects.update_or_create(
                league_id=League.objects.filter(name=column[32])[0].id,
                name=column[31]
            )
        _, created = Player.objects.update_or_create(
            team_id=2,
            name=column[0],
            age=column[2],
            position=column[1],
            minutes=column[3],
            accurate_passes=float(column[4])/float(column[3])*90,
            passes=float(column[5])/float(column[3])*90,
            created_situations=float(column[6])/float(column[3])*90,
            key_passes=float(column[7])/float(column[3])*90,
            dribble=float(column[8])/float(column[3])*90,
            fouls_on=float(column[9])/float(column[3])*90,
            offsides=float(column[10])/float(column[3])*90,
            mistakes=float(column[11])/float(column[3])*90,
            culpable_goals=float(column[12])/float(column[3])*90,
            accurate_cross=float(column[13])/float(column[3])*90,
            assists=float(column[14])/float(column[3])*90,
            heads=float(column[15])/float(column[3])*90,
            tackles=float(column[16])/float(column[3])*90,
            key_heads=float(column[17])/float(column[3])*90,
            interceptions=float(column[18])/float(column[3])*90,
            catch_saves=float(column[19])/float(column[3])*90,
            saves=float(column[20])/float(column[3])*90,
            saves_on_corner=float(column[21])/float(column[3])*90,
            complete_tackles=float(column[22])/float(column[3])*90,
            accurate_shots=float(column[23])/float(column[3])*90,
            shots=float(column[24])/float(column[3])*90,
            key_tackles=float(column[25])/float(column[3])*90,
            win_heads=float(column[26])/float(column[3])*90,
            goals=float(column[27])/float(column[3])*90,
            crosses=float(column[28])/float(column[3])*90,
            rating=float(column[29]),
            club=column[31],
            league=column[32],
            rate=rate(column)
        )

    context = {}
    return render(request, template, context)


@permission_required('admin.can_addlog_entry')
def player_delete(request):
    Player.objects.all().delete()
    return redirect('player_upload')


@permission_required('admin.can_addlog_entry')
def player_club_delete(request, club):
    Player.objects.filter(club=club).delete()
    return redirect('players')


@permission_required('admin.can_addlog_entry')
def player_league_delete(request, league):
    Player.objects.filter(league=league).delete()
    return redirect('players')

import json
import traceback

from django.contrib import messages
from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render, redirect

from wallOf.forms import *
from wallOf.models import *


def redirect_back(request, redirect_here):
    render(request, 'wallOf/check.html')
    return redirect(redirect_here)


def display_menu(request):
    return render(request, 'wallOf/menu.html')


def frustrations(request):
    posts = Posts

    # all_ranked_by_votes = ModelPosts.objects.annotate(biggest=F('up_vote') + F('down_vote')).order_by('biggest',
    #                                                                                                   'date_and_time')

    all_ranked_by_votes = ModelPosts.objects.order_by('date_and_time')

    all_ranked_by_votes = reversed(all_ranked_by_votes)

    if request.method == 'POST' and not request.is_ajax() and 'postings' in request.POST:
        try:
            form = Posts(request.POST)
            if form.is_valid():
                form.clean()
                form.save()
                messages.success(request, 'Post Saved!')
                # return redirect('redirect_for_frustrations')
                return redirect_back(request, 'frustrations')

        except Exception as e:
            # messages.error(request, 'Error')
            messages.error(request, 'Error')
            print(e)
            print(traceback)
            print(e.__traceback__)
            return render(request, 'wallOf/frustrations.html', context={'postF': posts, 'all': all_ranked_by_votes})

    if request.method == 'POST' and not request.is_ajax() and 'comment' in request.POST:
        print(request.POST)

    if request.is_ajax() and request.method == 'POST':
        try:
            ajax_received = json.loads(request.body.decode('utf-8'))

            if ajax_received['Name'] == 'up_voted_It':
                current_ups = ModelPosts.objects.filter(pk=(int(ajax_received['Value']) - 3669)).values('up_vote')[0][
                    'up_vote']

                ModelPosts.objects.filter(pk=(int(ajax_received['Value']) - 3669)).update(up_vote=current_ups + 1)
            if ajax_received['Name'] == 'down_voted_It':
                current_down = \
                    ModelPosts.objects.filter(pk=(int(ajax_received['Value']) - 3669)).values('down_vote')[0][
                        'down_vote']
                ModelPosts.objects.filter(pk=(int(ajax_received['Value']) - 3669)).update(down_vote=current_down - 1)

            # if ajax_received['Name'] == 'comment':
            #     the_post = ModelPosts.objects.filter(pk=(int(ajax_received['Value']) - 3669))
            #
            #     comments = ModelComment(
            #         comment=ajax_received['textarea'],
            #         content_type=ContentType.objects.get_for_model(ModelPosts),
            #         object_id=(int(ajax_received['Value']) - 3669)
            #     )
            #     comments.clean()
            #     comments.save()

            response = JsonResponse({"success": "success was there"})
            response.status_code = 200  # To announce that the user isn't allowed to publish
            return response

        except Exception as e:
            # messages.error(request, 'Error')
            print(e)
            print(traceback)
            print(e.__traceback__)

        response = JsonResponse({"success": "success was there"})
        response.status_code = 400  # To announce that the user isn't allowed to publish
        return response

        # return render(request, 'wallOf/frustrations.html', context={'postF': posts, 'all': all_ranked_by_votes})

    return render(request, 'wallOf/frustrations.html',
                  context={'postF': posts, 'all': all_ranked_by_votes,
                           # 'commentF': Comment
                           })


def secretView(request):
    posts = secrets

    all_ranked_by_votes = Modelsecrets.objects.annotate(biggest=F('up_vote') + F('down_vote')).order_by('biggest', 'date_and_time')

    all_ranked_by_votes = reversed(all_ranked_by_votes)

    if request.method == 'POST' and not request.is_ajax():
        try:
            form = secrets(request.POST)
            if form.is_valid():
                form.clean()
                form.save()
                messages.success(request, 'Post Saved!')
                # need to fix this part
                # return redirect('redirect_for_secret')
                return redirect_back(request, 'secrets')

        except Exception as e:
            messages.error(request, 'Error')
            print(e)
            print(traceback)
            print(e.__traceback__)
            return render(request, 'wallOf/secret.html', context={'postF': posts, 'all': all_ranked_by_votes})

    if request.is_ajax() and request.method == 'POST':
        try:
            ajax_received = json.loads(request.body.decode('utf-8'))

            if ajax_received['Name'] == 'up_voted_It':
                current_ups = \
                    Modelsecrets.objects.filter(pk=(int(ajax_received['Value']) - 3669)).values('up_vote')[0][
                        'up_vote']

                Modelsecrets.objects.filter(pk=(int(ajax_received['Value']) - 3669)).update(up_vote=current_ups + 1)
            if ajax_received['Name'] == 'down_voted_It':
                current_down = \
                    Modelsecrets.objects.filter(pk=(int(ajax_received['Value']) - 3669)).values('down_vote')[0][
                        'down_vote']
                Modelsecrets.objects.filter(pk=(int(ajax_received['Value']) - 3669)).update(down_vote=current_down - 1)

            response = JsonResponse({"success": "success was there"})
            response.status_code = 200  # To announce that the user isn't allowed to publish
            return response

        except Exception as e:
            # messages.error(request, 'Error')
            messages.error(request, 'Error')
            print(e)
            print(traceback)
            print(e.__traceback__)
            response = JsonResponse({"success": "success was there"})
            response.status_code = 400  # To announce that the user isn't allowed to publish
            return response

            # return render(request, 'wallOf/secret.html', context={'postF': posts, 'all': all_ranked_by_votes})

    return render(request, 'wallOf/secret.html', context={'postF': posts, 'all': all_ranked_by_votes})


def advice_view(request):
    posts = advice

    all_ranked_by_votes = ModelAdvice.objects.annotate(biggest=F('up_vote') + F('down_vote')).order_by('biggest',
                                                                                                       'date_and_time')

    all_ranked_by_votes = reversed(all_ranked_by_votes)

    if request.method == 'POST' and not request.is_ajax():
        try:
            form = advice(request.POST)
            if form.is_valid():
                form.clean()
                form.save()
                messages.success(request, 'Post Saved!')

                return redirect_back(request, 'wisdom')

        except Exception as e:
            # messages.error(request, 'Error')
            messages.error(request, 'Error')
            print(e)
            print(traceback)
            print(e.__traceback__)
            return render(request, 'wallOf/advice.html', context={'postF': posts, 'all': all_ranked_by_votes})

    if request.is_ajax() and request.method == 'POST':
        try:
            ajax_received = json.loads(request.body.decode('utf-8'))

            if ajax_received['Name'] == 'up_voted_It':
                current_ups = \
                    ModelAdvice.objects.filter(pk=(int(ajax_received['Value']) - 3669)).values('up_vote')[0][
                        'up_vote']

                ModelAdvice.objects.filter(pk=(int(ajax_received['Value']) - 3669)).update(up_vote=current_ups + 1)
            if ajax_received['Name'] == 'down_voted_It':
                current_down = \
                    ModelAdvice.objects.filter(pk=(int(ajax_received['Value']) - 3669)).values('down_vote')[0][
                        'down_vote']
                ModelAdvice.objects.filter(pk=(int(ajax_received['Value']) - 3669)).update(down_vote=current_down - 1)

            response = JsonResponse({"success": "success was there"})
            response.status_code = 200  # To announce that the user isn't allowed to publish
            return response

        except Exception as e:
            messages.error(request, 'Error')
            print(e)
            print(traceback)
            print(e.__traceback__)
            response = JsonResponse({"success": "success was there"})
            response.status_code = 400  # To announce that the user isn't allowed to publish
            return response

            # return render(request, 'wallOf/secret.html', context={'postF': posts, 'all': all_ranked_by_votes})

    return render(request, 'wallOf/advice.html', context={'postF': posts, 'all': all_ranked_by_votes})

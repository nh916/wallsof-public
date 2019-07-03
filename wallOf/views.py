import json
import traceback

from django.contrib import messages
from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from wallOf.forms import *
from wallOf.models import *


# def redirect_for_frustrations(request):
#     # render(request, 'wallOf/wall.html')
#     render(request, 'wallOf/check.html')
#     return redirect('frustrations')
#
#
# def redirect_to_secrete(request):
#     render(request, 'wallOf/check.html')
#     return redirect('secretes')


def redirect_back(request, redirect_here):
    render(request, 'wallOf/check.html')
    return redirect(redirect_here)


def display_menu(request):
    return render(request, 'wallOf/menu.html')


def frustrations(request):
    posts = Posts

    all_ranked_by_votes = ModelPosts.objects.annotate(biggest=F('up_vote') + F('down_vote')).order_by('biggest',
                                                                                                      'date_and_time')

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
            print(e)
            return render(request, 'wallOf/frustrations.html', context={'postF': posts, 'all': all_ranked_by_votes})

    if request.is_ajax() and request.method == 'POST':
        # try:
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




            if ajax_received['Name'] == 'comment':
                the_post = ModelPosts.objects.filter(pk=(int(ajax_received['Value']) - 3669))

                comments = ModelComment(
                    comment=ajax_received['textarea'],
                    content_type=ContentType.objects.get_for_model(ModelPosts),
                    object_id=(int(ajax_received['Value']) - 3669)
                )
                comments.clean()
                comments.save()

            response = JsonResponse({"success": "success was there"})
            response.status_code = 200  # To announce that the user isn't allowed to publish
            return response

        # except Exception as e:
        #     # messages.error(request, 'Error')
        #     print(e)
        #     print(traceback)
        #     print(e.__traceback__)

            response = JsonResponse({"success": "success was there"})
            response.status_code = 400  # To announce that the user isn't allowed to publish
            return response












            # return render(request, 'wallOf/frustrations.html', context={'postF': posts, 'all': all_ranked_by_votes})

    return render(request, 'wallOf/frustrations.html',
                  context={'postF': posts, 'all': all_ranked_by_votes, 'commentF': Comment})


def secreteView(request):
    posts = secretes

    all_ranked_by_votes = ModelSecretes.objects.annotate(biggest=F('up_vote') + F('down_vote')).order_by('biggest',
                                                                                                         'date_and_time')

    all_ranked_by_votes = reversed(all_ranked_by_votes)

    if request.method == 'POST' and not request.is_ajax():
        try:
            form = secretes(request.POST)
            if form.is_valid():
                form.clean()
                form.save()
                messages.success(request, 'Post Saved!')
                # need to fix this part
                # return redirect('redirect_for_secrete')
                return redirect_back(request, 'secretes')


        except Exception:
            # messages.error(request, 'Error')
            return render(request, 'wallOf/secrete.html', context={'postF': posts, 'all': all_ranked_by_votes})

    if request.is_ajax() and request.method == 'POST':
        try:
            ajax_received = json.loads(request.body.decode('utf-8'))

            if ajax_received['Name'] == 'up_voted_It':
                current_ups = \
                    ModelSecretes.objects.filter(pk=(int(ajax_received['Value']) - 3669)).values('up_vote')[0][
                        'up_vote']

                ModelSecretes.objects.filter(pk=(int(ajax_received['Value']) - 3669)).update(up_vote=current_ups + 1)
            if ajax_received['Name'] == 'down_voted_It':
                current_down = \
                    ModelSecretes.objects.filter(pk=(int(ajax_received['Value']) - 3669)).values('down_vote')[0][
                        'down_vote']
                ModelSecretes.objects.filter(pk=(int(ajax_received['Value']) - 3669)).update(down_vote=current_down - 1)

            response = JsonResponse({"success": "success was there"})
            response.status_code = 200  # To announce that the user isn't allowed to publish
            return response

        except Exception:
            # messages.error(request, 'Error')
            response = JsonResponse({"success": "success was there"})
            response.status_code = 400  # To announce that the user isn't allowed to publish
            return response

            # return render(request, 'wallOf/secrete.html', context={'postF': posts, 'all': all_ranked_by_votes})

    return render(request, 'wallOf/secrete.html', context={'postF': posts, 'all': all_ranked_by_votes})


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

                return redirect_back(request, 'advice')


        except Exception:
            # messages.error(request, 'Error')
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

        except Exception:
            # messages.error(request, 'Error')
            response = JsonResponse({"success": "success was there"})
            response.status_code = 400  # To announce that the user isn't allowed to publish
            return response

            # return render(request, 'wallOf/secrete.html', context={'postF': posts, 'all': all_ranked_by_votes})

    return render(request, 'wallOf/advice.html', context={'postF': posts, 'all': all_ranked_by_votes})

# class create_post(CreateView):
#     model = ModelPosts
#     fields = [
#         'title',
#         'emotion',
#     ]
#     template_name = 'wallOf/frustrations.html'
#
#     def get_form(self, form_class=None):
#         if form_class is None:
#             form_class = self.get_form_class()
#
#         form = super(create_post, self).get_form(form_class)
#         form.fields['emotion'].widget.attrs = {'cols': 40, 'rows': 20, 'placeholder': 'tell me'}
#         return form


# class update_vote(UpdateView):
#     model = ModelPosts
#     fields = [
#         # 'vote',
#         'up_vote',
#         'down_vote',
#     ]
#     template_name = 'wallOf/frustrations.html'

# def get_form(self, form_class=None):
#     if form_class is None:
#         form_class = self.get_form_class()
#
#     form = super(update_vote, self).get_form(form_class)
#     form.fields['vote'].widget = form.RadioSelect
#     return form

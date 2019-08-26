from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, UpdateView, ListView
from django.template.defaulttags import register
from donor_app.models import Donor
from django.db.models import Q


@register.filter
def get_blood_group(bgroup):
    if bgroup in Donor.bgroup_choices:
        return Donor.bgroup_choices[bgroup]
    else:
        return bgroup
    
@register.filter
def to_str(value):
    return str(value)
    


class HomePage(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)


        context['blood_group_choices'] = []
        
        for id, group in Donor.bgroup_choices.items():
            arr = [id, group, Donor.objects.filter(blood_group=id, is_private=False, is_closed=False).count()]
            context['blood_group_choices'].append(arr)

        return context


class SearchPage(ListView):
    template_name = 'searchpage.html'
    model = Donor
    paginate_by = 50

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['blood_group_choices'] = Donor.bgroup_choices

        if 'page' in self.kwargs:
            context['page_obj'].page = self.kwargs.get('page')

        context['query_string'] = "&".join(map(lambda x: x[0] + "=" + x[1], self.request.GET.items()))
        context['blood_group_choices'] = []
        
        for id, group in Donor.bgroup_choices.items():
            arr = [id, group, Donor.objects.filter(blood_group=id).count()]
            context['blood_group_choices'].append(arr)

        return context

    def get_queryset(self):
        qs = super().get_queryset()

        group = self.request.GET.get('g')
        gender = self.request.GET.get('s')
        order_by = self.request.GET.get('o')
        keyword = self.request.GET.get('q', '').strip()

        if keyword:
            qs = qs.filter(Q(first_name__icontains=keyword) | Q(last_name__icontains=keyword))
        

        if group:
            qs = qs.filter(blood_group=group)

        if gender:
            qs = qs.filter(gender=gender)

        if order_by == "1":
            qs = qs.order_by('first_name', 'last_name')
        elif order_by == "2":
            qs = qs.order_by('-first_name', '-last_name')
        elif order_by == "3":
            qs = qs.order_by("blood_price_per_100gramm")
        elif order_by == "4":
            qs = qs.order_by("-blood_price_per_100gramm")
        else:
            qs = qs.order_by("?")



        return qs.filter(is_private=False, is_closed=False)

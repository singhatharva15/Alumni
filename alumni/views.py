from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import auth
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from certificate_template.cg import generate_certificate as cg

from alumni.models import Opportunities, Career, Events, UserCert
from alumni.forms import CareerForm, ProfileForm
from accounts.models import User


# Profile view
@login_required
def profile(request):
    return render(request,"index.html", {})

# update profile view
class UpdateProfile(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'editprofile.html'
    success_url = reverse_lazy('profile')

    def get_success_url(self):
        messages.success(self.request, 'Profile Updated Successfully')
        return reverse_lazy('profile')


# career list and create view
class CareerCreateView(LoginRequiredMixin, CreateView):
    model = Career
    form_class = CareerForm
    template_name = 'career.html'

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Career.objects.all()
        return super(CareerCreateView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        messages.success(self.request, 'Recored Inserted Successfully')
        return reverse_lazy('career')


# experience update view
class UpdateExperice(LoginRequiredMixin, UpdateView):
    model = Career
    form_class = CareerForm
    template_name = 'update-experience.html'

    def get_success_url(self):
        messages.success(self.request, 'Recored Inserted Successfully')
        return reverse_lazy('career')

# career delete view
@login_required
def destroyBatch(request, pk):  
    car = Career.objects.get(pk=pk)  
    car.delete()  
    messages.success(request, 'Recored Deleted Successfully')
    return redirect('career',)


@login_required
def events(request):
    even= Events.objects.all()
    return render(request,"events.html",{'events': even})


@login_required
def opportunity(request):
    opp= Opportunities.objects.all()
    return render(request,"opportunity.html",{'opps': opp})


# generate certificate
# def generate_certificate(request):
#     try:
#         cert_obj = get_object_or_404(UserCert, user=request.user)
#         if cert_obj.show_cert:
#             img = cg(cert_obj.display_name)
#             response = HttpResponse(content_type="image/png")
#             img.save(response, "PNG")
#             return response
#         else:
#             return HttpResponse("Certificate generation failed. Please contact Administator.")
#     except Exception as e:
#         print(e)
#         return HttpResponse("Certificate generation failed. Please contact Administator.")

def generate_certificate(request):
    img = cg(f"{request.user.first_name} {request.user.last_name}")
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response
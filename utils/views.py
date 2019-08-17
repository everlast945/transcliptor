from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView


class CustomListView(ListView):
    pass


class RegisterView(CustomListView):
    template_name = 'bases/base_register.html'


class CustomDetailView(DetailView):
    pass


class CustomCreateView(CreateView):
    pass


class CustomUpdateView(UpdateView):
    pass


class CustomDeleteView(DeleteView):
    pass

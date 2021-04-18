from .forms import LogForm


def GetLoginForm(request):
    return {"login": LogForm}
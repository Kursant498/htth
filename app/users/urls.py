from rest_framework.routers import DefaultRouter
from app.users.views import RegisterViewSet, LoginViewSet, LogoutViewSet, UserAuthenticatedViewSet

router = DefaultRouter()

router.register("register", RegisterViewSet, basename="register")
router.register("login", LoginViewSet, basename="login")
router.register("logout", LogoutViewSet, basename="logout")
router.register("userauth", UserAuthenticatedViewSet, basename="userauth")
urlpatterns = router.urls
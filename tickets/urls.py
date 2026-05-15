from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('tickets/', views.api_tickets),

    path('tickets/<int:ticket_id>/', views.editar_ticket),

    path('tickets/<int:ticket_id>/comentarios/', views.crear_comentario),
    # 🔐 JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
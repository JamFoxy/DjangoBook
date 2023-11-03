from django.urls import path
from . import views

urlpatterns = [
#     path('', views.book_view),
#     path('book_detail/<int:id>/', views.book_detail_view),
#     path('book_list/', views.book_delete_view),
#     path('book_list/<int:id>/delete/', views.book_drop_view),
#     path('create_book/', views.createBookPostView),
#     path('add-cooment/', views.createBookReview),
# ]

    path("", views.BookView.as_view()),
    path("book_list", views.BookListView.as_view()),
    path('book_detail/<int:id>/', views.BookDetailView.as_view()),
    path('book_list/<int:id>/delete/', views.BookDropView.as_view()),
    path('book_list/<int:id>/update/', views.UpdateBookView.as_view()),
    path('create_book/', views.CreateBookView.as_view()),
    path('add-comment/', views.createBookReview),
    path('search/', views.SearchView.as_view(), name='search'),
]
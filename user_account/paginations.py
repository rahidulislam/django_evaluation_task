from rest_framework.pagination import PageNumberPagination

class UserListPagination(PageNumberPagination):
    page_size = 5  # Customize the page size here
    page_size_query_param = 'page_size'
    max_page_size = 100
from rest_framework import pagination


class EmployeeListPaginationClass(pagination.PageNumberPagination):
    page_size = 20

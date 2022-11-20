from rest_framework import pagination
from rest_framework.response import Response


class AppPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response(data)

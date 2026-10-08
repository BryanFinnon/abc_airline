from rest_framework import status
from rest_framework.test import APITestCase


class RouteApiTests(APITestCase):
    def test_create_and_list_route(self):
        create_response = self.client.post(
            "/api/routes/",
            {"departure": "London", "arrival": "Abidjan"},
            format="json",
        )

        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(create_response.data["departure"], "London")

        list_response = self.client.get("/api/routes/")
        self.assertEqual(list_response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(list_response.data), 1)

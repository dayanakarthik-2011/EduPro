class Status200Response(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '[{"label": "string", "field_type": "Text"}]',
            "response_serializer": "Status_200Serializer",
            "response_serializer_import_str": "from type_form.build.view_environments.get_form_fields.get_form_fields.responses.Status_200.Status_200.Status_200Serializer import Status_200Serializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass
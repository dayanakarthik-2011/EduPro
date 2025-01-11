from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions import custom_exceptions
from typing import Optional
from amazon.interactors.storage_interfaces.dtos import EmiDTO


class ItemEmiInteractor:

    def __init__(self, storage:StorageInterface, presenter:PresenterInterface):

        self.storage = storage
        self.presenter = presenter


    def create_debit_card_emi(self, emi_dto:EmiDTO):
        """ELP
            -validate input details
                -validate emi_type
                -validate card_name
                -validate minimum_purchase_value
                -validate number_of_months
                -validate interest_in_rupees
                -validate interest_in_percentage
                -validate total_amount
            -check if emi exists
            create debit card emi
        """
        self._validate_input_details_for_debit_card_emi(emi_dto=emi_dto)

        try:
            self.storage.check_if_emi_already_exists(emi_dto=emi_dto)
        except custom_exceptions.EmiAlreadyExistsException:
            self.presenter.raise_exception_for_emi_already_exists()

        emi_id = self.storage.create_debit_card_emi(emi_dto=emi_dto)

        return self.presenter.get_response_for_create_debit_card_emi(emi_id=emi_id)
        
    def _validate_input_details_for_debit_card_emi(self, emi_dto:EmiDTO):
        
        emi_type_not_present = not emi_dto.emi_type
        if emi_type_not_present:
            self.presenter.raise_exception_for_missing_emi_type()

        card_name_not_present = not emi_dto.card_name
        if card_name_not_present:
            self.presenter.raise_exception_for_missing_card_name()

        number_of_months_not_present = not emi_dto.number_of_months
        if number_of_months_not_present:
            self.presenter.raise_exception_for_missing_number_of_months()

        interest_in_rupees_not_present = not emi_dto.interest_in_rupees
        if interest_in_rupees_not_present:
            self.presenter.raise_exception_for_missing_interest_in_rupees()

        interest_in_percentage_not_present = not emi_dto.interest_in_percentage
        if interest_in_percentage_not_present:
            self.presenter.raise_exception_for_missing_interest_in_percentage()

        total_amount_not_present = not emi_dto.total_amount
        if total_amount_not_present:
            self.presenter.raise_exception_for_missing_total_amount()

    def create_no_cost_emi(self, emi_dto:EmiDTO):

        """ELP
            -validate input details
                -validate emi_type
                -validate debit_card_name
                -validate minimum_purchase_value
                -validate number_of_months
                -validate interest_in_rupees
                -validate interest_in_percentage
                -validate total_amount
            -check if emi exists
            -create no cost emi
        """
        
        self._validate_input_details_for_no_cost_emi(emi_dto=emi_dto)

        try:
            self.storage.check_if_emi_already_exists(emi_dto=emi_dto)
        except custom_exceptions.EmiAlreadyExistsException:
            self.presenter.raise_exception_for_emi_already_exists()

        emi_id = self.storage.create_no_cost_emi(emi_dto=emi_dto)

        return self.presenter.get_response_for_create_no_cost_emi(emi_id=emi_id)
    
    def _validate_input_details_for_no_cost_emi(self, emi_dto:EmiDTO):
        
        emi_type_not_present = not emi_dto.emi_type
        if emi_type_not_present:
            self.presenter.raise_exception_for_missing_emi_type()

        card_name_not_present = not emi_dto.card_name
        if card_name_not_present:
            self.presenter.raise_exception_for_missing_card_name()

        number_of_months_not_present = not emi_dto.number_of_months
        if number_of_months_not_present:
            self.presenter.raise_exception_for_missing_number_of_months()

        interest_in_rupees_not_present = not emi_dto.interest_in_rupees
        if interest_in_rupees_not_present:
            self.presenter.raise_exception_for_missing_interest_in_rupees()

        interest_in_percentage_not_present = not emi_dto.interest_in_percentage
        if interest_in_percentage_not_present:
            self.presenter.raise_exception_for_missing_interest_in_percentage()

        total_amount_not_present = not emi_dto.total_amount
        if total_amount_not_present:
            self.presenter.raise_exception_for_missing_total_amount()


    def create_other_emi_type(self, emi_dto:EmiDTO):
        
        """ELP
            -check if emi exists
            -create other emi type
        """
        try:
            self.storage.check_if_emi_already_exists(emi_dto=emi_dto)
        except custom_exceptions.EmiAlreadyExistsException:
            self.presenter.raise_exception_for_emi_already_exists()

        emi_id = self.storage.create_other_emi_type(emi_dto=emi_dto)

        return self.presenter.get_response_for_create_other_emi_type(emi_id=emi_id)

    
    def add_emi_to_item(self, item_id:int, emi_id:int):

        """ELP
            -validate input details
                -validate item_id
                -validate emi_id
            -check if item exists
            -check if emi exists
            -add emi to item
        """

        self._validate_input_details_for_add_emi_to_item(item_id=item_id, emi_id=emi_id)

        self._check_if_given_input_data_is_correct(item_id=item_id, emi_id=emi_id)

        item_emi_id = self.storage.add_emi_to_item(item_id=item_id, emi_id=emi_id)

        return self.presenter.get_response_for_add_emi_to_item(item_emi_id=item_emi_id)
    
    def _validate_input_details_for_add_emi_to_item(self, item_id:int, emi_id:int):

        item_id_not_present = not item_id
        if item_id_not_present:
            self.presenter.raise_exception_for_missing_item_id()

        emi_id_not_present = not emi_id
        if emi_id_not_present:
            self.presenter.raise_exception_for_missing_emi_id()

    def _check_if_given_input_data_is_correct(self, item_id:int, emi_id:int):

        try:
            self.storage.check_if_item_exists(item_id=item_id)
        except custom_exceptions.ItemDoesNotExistException:
            self.presenter.raise_exception_for_item_does_not_exist()

        try:
            self.storage.check_if_emi_exists(emi_id=emi_id)
        except custom_exceptions.EmiDoesNotExistException:
            self.presenter.raise_exception_for_emi_does_not_exist()

    
    def add_item_emi_to_order(self, order_id:int, item_emi_id:int):

        """ELP
            -check if order exists
            -check if item emi exists
            -check if item emi is associated with item
            -check if item emi is not already added to order
            -add item emi to order
        """

        self._check_if_input_data_is_correct_for_add_item_emi_to_order(order_id=order_id, item_emi_id=item_emi_id)

        self.storage.add_item_emi_to_order(order_id=order_id, item_emi_id=item_emi_id)

        return self.presenter.get_response_for_add_item_emi_to_order()
    
    def _check_if_input_data_is_correct_for_add_item_emi_to_order(self, order_id:int, item_emi_id:int):

        try:
            self.storage.check_if_order_exists(order_id=order_id)
        except custom_exceptions.OrderDoesNotExistException:
            self.presenter.raise_exception_for_order_does_not_exist()

        try:
            self.storage.check_if_item_emi_exists(item_emi_id=item_emi_id)
        except custom_exceptions.ItemEmiDoesNotExistException:
            self.presenter.raise_exception_for_item_emi_does_not_exist()

        try:
            self.storage.check_if_item_emi_is_associated_with_item(order_id=order_id, item_emi_id=item_emi_id)
        except custom_exceptions.ItemEmiIsNotAssociatedWithItemException:
            self.presenter.raise_exception_for_item_emi_is_not_associated_with_item()

        try:
            self.storage.check_if_item_emi_is_not_already_added_to_order(order_id=order_id, item_emi_id=item_emi_id)
        except custom_exceptions.ItemEmiAlreadyAddedToOrderException:
            self.presenter.raise_exception_for_item_emi_already_added_to_order()
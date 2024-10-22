"""Модуль описаний констант для модуля системных роутеров"""

CREATE_REDUCED_URL_DESC = "Запрос на создание короткой ссылки"
DELETE_REDUCED_URL_DESC = "Запрос на удаление полной ссылки по короткой ссылке"
GET_FULL_BY_REDUCED_URL_DESC = "Запрос на получение полной ссылки по короткой ссылке"


CREATE_REDUCED_URL_PATH = "/create_reduced_url"
DELETE_REDUCED_URL_PATH = "/delete_reduced_url"
GET_FULL_BY_REDUCED_URL_PATH = "/{short_url}"

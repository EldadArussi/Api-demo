from Infra.BaseTest import BaseTest
from Infra.Verifications import Verifications
from Pages.Controls import Controls
from Pages.DateWidgets import DateWidgets
from Pages.Dialog import Dialog
from Pages.Grid import Grid
from Pages.IconGrid import IconGrid
from Pages.LightTheme import LightTheme
from Pages.Lobby import Lobby
from Pages.Views import Views


class TestsVia(BaseTest):
    def test_verify_date(self, init_app):
        expected_date = "2-1-2023 12:00"
        self.driver = init_app
        self.lobby = Lobby(self.driver)
        self.lobby.click_on_views_screen()

        self.views = Views(self.driver)
        self.views.click_on_data_widgets()

        self.dateWidgets = DateWidgets(self.driver)
        self.dateWidgets.click_on_dialog()

        self.dialog = Dialog(self.driver)
        self.dialog.change_date()
        self.dialog.change_time()
        actual_date = self.dialog.get_date_time()
        Verifications.compare_two_values(actual_date,expected_date)

    def test_count_all_icons(self, init_app):
        expected_count = 61
        self.driver = init_app
        self.lobby = Lobby(self.driver)
        self.lobby.click_on_views_screen()

        self.views = Views(self.driver)
        self.views.click_on_grid()

        self.grid = Grid(self.driver)
        self.grid.click_on_icon_grid()

        self.iconGrid = IconGrid(self.driver)
        actual_count = self.iconGrid.get_count_icon_grid()
        Verifications.compare_two_values(actual_count,expected_count)

    def test_fill_data(self, init_app):

        name = "Eldad Arussi"
        self.driver = init_app
        self.lobby = Lobby(self.driver)
        self.lobby.click_on_views_screen()

        self.views = Views(self.driver)
        self.views.click_on_controls()

        self.controls = Controls(self.driver)
        self.controls.click_on_light_theme()

        self.lightTheme = LightTheme(self.driver)
        self.lightTheme.set_input_field(name)
        self.lightTheme.check_check_box_2()
        self.lightTheme.select_radio_btn()
        self.lightTheme.select_jupiter_planet()
        self.lightTheme.click_on_save()






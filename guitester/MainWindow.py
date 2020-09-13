import tkinter
from tkinter import ttk

class AppWindow:
    main_window = None
    platform_list = None
    device_list = None
    app_list = None
    is_hardware = None
    run_button = None

    platform_options = ['iOS', 'Android'] # Platforms for testing
    ios_device_options = {
        False: ['iPhone SE (2nd generation)'], # Simulated device options
        True: ['No Device'] # Hardware iOS device options
    }
    android_device_options = {
        False: ['Pixel_3a_API_29'], # AVD options to choose from
        True: []  # Real devices to choose from
    }
    device_options = {
        'ios': ios_device_options,
        'android': android_device_options
    }

    is_hw = None
    selected_platform = None
    selected_device = None
    selected_app = None

    test_app_lists = {
        'ios': ['TestApp.app.zip', 'GuineaPig-sim-debug.app.zip'],
        'android': ['ApiDemos-debug.apk', 'GuineaPigApp-debug.apk']
    }


    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.configure(background = 'SystemButtonFace')
        self.main_window.title('Pytest Appium script GUI runner')

        self.is_hw = tkinter.BooleanVar()
        self.selected_device = tkinter.StringVar()
        self.selected_platform = tkinter.StringVar()
        self.selected_app = tkinter.StringVar()

        ttk.Label(self.main_window, text = "Set up the test").grid(row = 0, column = 0, columnspan = 4)

        ttk.Label(self.main_window, text = "Platform ", background = 'SystemButtonFace').grid(row = 1, column = 0)
        self.platform_list = ttk.Combobox(
            self.main_window,
            values = self.platform_options,
            textvariable = self.selected_platform
        )
        self.platform_list.grid(row = 1, column = 1)
        self.platform_list.bind('<<ComboboxSelected>>', self.platform_change)
        self.platform_list.current(0)

        ttk.Label(self.main_window, text = "Device ", background = 'SystemButtonFace').grid(row = 2, column = 0)
        self.device_list = ttk.Combobox(
            self.main_window,
            values = self.device_options[self.selected_platform.get().lower()][self.is_hw.get()],
            textvariable = self.selected_device
        )
        self.device_list.grid(row = 2, column = 1)
        self.device_list.bind('<<ComboboxSelected>>', self.device_change)
        self.device_list.current(0)
        self.is_hardware = ttk.Checkbutton(
            self.main_window,
            variable = self.is_hw,
            onvalue = True,
            offvalue = False,
            command = self.physical_change
        )
        self.is_hardware.grid(row = 2, column = 2)
        self.is_hw.set(False)
        ttk.Label(self.main_window, text = 'Physical device', background = 'SystemButtonFace').grid(row = 2, column = 3)

        ttk.Label(self.main_window, text = "App ", background = 'SystemButtonFace').grid(row = 3, column = 0)
        self.app_list = ttk.Combobox(
            self.main_window,
            values = self.test_app_lists[self.selected_platform.get().lower()],
            textvariable = self.selected_app
        )
        self.app_list.grid(row = 3, column = 1)
        self.app_list.current(0)

        self.run_button = ttk.Button(self.main_window, text = "Run PyTest")
        self.run_button.grid(row = 4, column = 2, columnspan = 2)
        self.run_button.configure(command = self.run_tests)


    def run(self):
        self.main_window.mainloop()


    def platform_change(self, event):
        print(f'Platform: {self.selected_platform.get()}')
        self.device_list['values'] = self.device_options[self.selected_platform.get().lower()][self.is_hw.get()]
        self.device_list.current(0)
        self.app_list['values'] = self.test_app_lists[self.selected_platform.get().lower()]
        self.app_list.current(0)


    def device_change(self, event):
        print(f'Device change: {self.selected_device.get()}')


    def physical_change(self):
        print(f'Hardware? {self.is_hw.get()}')


    def run_tests(self):
        print('Running tests with parameters:')
        print(f'\tPlatform: {self.selected_platform.get()}')
        print(f'\tDevice: {self.selected_device.get()}')
        print(f'\tHardware device: {self.is_hw.get()}')
        print(f'\tApp: {self.selected_app.get()}')

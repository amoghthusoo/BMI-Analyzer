screens = '''

ScreenManager:
    HomeScreen:
    DeveloperScreen:
    InfoScreen:
    HelpScreen:
    
        

<HomeScreen>:

    
    name : 'home'
    
    Screen:
        
        NavigationLayout:
            
            ScreenManager:
                
                Screen:
                    
                    BoxLayout:

                        orientation : 'vertical'
                        spacing : '15dp'

                        MDToolbar:
                            title : 'BMI Calculator'
                            left_action_items : [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                            right_action_items : [['dots-vertical', lambda x: nav_drawer.toggle_nav_drawer() ]]
                            elevation : 10
                            pos_hint : {'center_y' : 0.96}
                        
                        

                        MDTextField:
                            id : person_name
                            hint_text : 'Enter Your Name'
                            helper_text : ''
                            helper_text_mode : 'on_focus'
                            icon_right : 'account'
                            icon_right_color : app.theme_cls.primary_color
                            size_hint_x : None
                            width : '300sp'
                            pos_hint : {'center_x' : 0.5, 'center_y' : 0.80}         
                        
                        MDTextField:
                            id : person_weight
                            hint_text : 'Enter Your Weight'
                            helper_text : 'in kilograms'
                            helper_text_mode : 'on_focus'
                            icon_right : 'weight'
                            icon_right_color : app.theme_cls.primary_color
                            size_hint_x : None
                            width : '300sp'
                            pos_hint : {'center_x' : 0.5, 'center_y' : 0.70}

                        MDTextField:
                            id : person_height
                            hint_text : 'Enter Your Height'
                            helper_text : 'in meters'
                            helper_text_mode : 'on_focus'
                            icon_right : 'arrow-up'
                            icon_right_color : app.theme_cls.primary_color
                            size_hint_x : None
                            width : '300sp'
                            pos_hint : {'center_x' : 0.5, 'center_y' : 0.60}

                        MDFillRoundFlatButton:
                            text : 'Calculate'
                            font_size : '18sp'
                            size_hint_y : None
                            height : '40dp'
                            pos_hint : {'center_x' : 0.5, 'center_y' : 0.50}
                            on_release : app.callback_calculate(person_name.text, person_weight.text, person_height.text)

                        MDBottomAppBar:
                            MDToolbar :
                                title : 'Help'
                                left_action_items : [['help-box', lambda x: app.callback_help()]]
                                mode : 'free-end'
                                icon : 'information-variant'
                                on_action_button : 
                                    root.manager.transition.direction = 'left'
                                    root.manager.current = 'info'

                                    
                                    
                                

                        Widget:
                
            MDNavigationDrawer:
                id : nav_drawer
                
                BoxLayout:
                    orientation : 'vertical'
                    padding : '10dp'

                    MDLabel:
                        text : 'BMI Calculator'
                        color : app.theme_cls.primary_color
                        halign : 'center'
                        font_style : 'H4'
                        size_hint_y : None
                        height : self.texture_size[1]

                    Widget:
                        size_hint : (1, 0.05)

                    MDList:

                        
                        OneLineIconListItem : 
                            text : 'Developer'
                            on_release:
                                root.manager.transition.direction = 'left'
                                root.manager.current = 'developer'

                            IconLeftWidget:
                                icon : 'android'
                            
                        OneLineIconListItem : 
                            text : 'Calculate'
                            on_release:
                                app.callback_calculate(person_name.text, person_weight.text, person_height.text)
                            IconLeftWidget:
                                icon : 'play' 
                        OneLineIconListItem : 
                            text : 'Info'
                            on_release:
                                root.manager.transition.direction = 'left'
                                root.manager.current = 'info'
                            IconLeftWidget:
                                icon : 'information-variant'
                        OneLineIconListItem : 
                            text : 'Help'
                            on_release:
                                root.manager.transition.direction = 'left'
                                root.manager.current = 'help'
                            IconLeftWidget:
                                icon : 'help'

                    Widget:
                    
        
<DeveloperScreen>:

    name : 'developer'
    
    BoxLayout:

        orientation : 'vertical'
        spacing : '15dp'
        
        MDToolbar:
            title : 'Developer'
            left_action_items : [['arrow-left', lambda x: app.callback_return_home()]]
            elevation : 10
            pos_hint : {'center_y' : 0.96}

        MDLabel:
            text : '    Application developed by Amogh Thusoo.'
            size_hint_y : None
            height : self.texture_size[1]

        MDLabel:
            text : '    © 2020 Amogh Thusoo'
            size_hint_y : None
            height : self.texture_size[1]

        Widget:

<InfoScreen>:

    name : 'info'

    Screen:
        BoxLayout:

            orientation : 'vertical'
            spacing : '15dp'
            
            MDToolbar:
                title : 'Information'
                left_action_items : [['arrow-left', lambda x: app.callback_return_home()]]
                elevation : 10
                pos_hint : {'center_y' : 0.96}

            

            MDLabel:
                text : "This is a simple BMI (Body Mass Index) calculator used to determine the person's BMI. Enter your name, weight and height to calculate your BMI !"
                size_hint_x : None
                size_hint_y : None
                width : '340dp'
                height : self.texture_size[1]
                halign : 'justify'
                pos_hint : {'center_x' : 0.5}
                
            MDLabel:
                text : '   © 2020 Amogh Thusoo'
                size_hint_y : None
                height : self.texture_size[1]

            Widget:
<HelpScreen>:

    name : 'help'

    Screen:
        BoxLayout:

            orientation : 'vertical'
            spacing : '15dp'
            
            MDToolbar:
                title : 'Help'
                left_action_items : [['arrow-left', lambda x: app.callback_return_home()]]
                elevation : 10
                pos_hint : {'center_y' : 0.96}

            

            MDLabel:
                text : "1. Enter your name, weight and height in the space provided."
                size_hint_x : None
                size_hint_y : None
                width : '340dp'
                height : self.texture_size[1]
                halign : 'justify'
                pos_hint : {'center_x' : 0.5}
            
            MDLabel:
                text : "2. Remember that you have to provide weight in kilograms and height in meters."
                size_hint_x : None
                size_hint_y : None
                width : '340dp'
                height : self.texture_size[1]
                halign : 'justify'
                pos_hint : {'center_x' : 0.5}

            MDLabel:
                text : "3. Click on Calculate button at the bottom or click the Calculate button from the menu bar."
                size_hint_x : None
                size_hint_y : None
                width : '340dp'
                height : self.texture_size[1]
                halign : 'justify'
                pos_hint : {'center_x' : 0.5}
                
            MDLabel:
                text : '   © 2020 Amogh Thusoo'
                size_hint_y : None
                height : self.texture_size[1]

            Widget:  
'''          


from flet import *
from custom_checkbox import CustomCheckBox

# Main function to set up the UI components
def main(page: Page):
    # Color definitions
    BG = '#041955'   # Background color
    FWG = '#97b4ff'  # Foreground color light
    FG = '#3450a1'   # Foreground color dark
    PINK = '@eb06ff' # Accent color (Pink)

    # Stack to create a circular profile avatar with gradient and image
    circle = Stack(
        controls=[
            Container(  # Base circle
                width=100,
                height=100,
                border_radius=50,
                bgcolor='white12'
            )
        ]
    )

    def show_search_bar(e):
        # Toggle the visibility of the search bar
        search_bar.visible = not search_bar.visible
        page.update()  # Refresh the UI to reflect the change

    # Create the search bar and assign it to a variable
    search_bar = SearchBar(
        width=150,
        height=50,
        view_elevation=5,
        bar_bgcolor=FWG,
        bar_overlay_color='white',
        bar_hint_text="task ...",
        visible=False,  # Initially hidden
        scale=transform.Scale(0.8)

    )

    # Function to shrink the secondary page size when an event occurs
    def shrink(e):
        page_2.controls[0].width = 120
        page_2.controls[0].scale = transform.Scale(0.8, alignment=alignment.center_left)
        page.update()

    # Function to reset the secondary page's size
    def undo_shrink(e):
        page_2.controls[0].width = 400
        page_2.controls[0].border_radius = 25
        page_2.controls[0].scale = transform.Scale(1, alignment=alignment.center_right)
        page.update()

    # View for creating a new task, represented by a small "x" button
    create_task_view = Container(
        content=Container(on_click=lambda _: page.go('/'),
                          height=40, width=40,
                          content=Text('x')
                          )
    )

    # List of tasks, scrollable and initially empty
    tasks = Column(
        height=400,
        scroll='auto',
    )

    # Adding 10 task items with custom checkboxes to the tasks list
    for i in range(10):
        tasks.controls.append(
            Container(
                height=70,
                width=400,
                bgcolor=BG,
                border_radius=25,
                padding=padding.only(left=20, top=25),
                content=CustomCheckBox(
                    color=PINK,
                    size=30,
                    label='Create interesting content!'
                )),
        )

    # Row container for holding category cards
    categories_card = Row(
        scroll='auto'
    )

    # Defining categories and adding them to the categories_card row
    categories = ['Business', 'Family', 'Friends']
    for i, category in enumerate(categories):
        categories_card.controls.append(
            Container(
                border_radius=20,
                bgcolor=BG,
                width=170,
                height=110,
                padding=15,
                content=Column(
                    controls=[
                        Text('40 Tasks'),  # Placeholder task count
                        Text(category),   # Category name
                        Container(
                            width=160,
                            height=5,
                            bgcolor='white12',
                            border_radius=20,
                            padding=padding.only(right=i * 30),
                            content=Container(
                                bgcolor=PINK,  # Progress bar
                            ),
                        )
                    ]
                )
            )
        )

    # Main content of the first page
    first_page_contents = Container(
        content=Column(
            controls=[
                Row(alignment='spaceBetween',
                    controls=[
                        Container(on_click=lambda e: shrink(e),
                                  content=Icon(icons.MENU)  # Shrink the secondary page
                                  ),
                        Row(
                            controls=[
                                Container(on_click=lambda e: show_search_bar(e),
                                          content=Icon(icons.SEARCH)  # Shrink the secondary page
                                          ),  # Search icon
                                search_bar,                                Icon(icons.NOTIFICATIONS_OUTLINED)  # Notifications icon
                            ],
                        ),
                    ],
                    ),
                Container(height=20),  # Space between menu and text
                Text(value=" Hi Joe !"),  # Greeting text
                Text(value='CATEGORIES'),  # Section title
                Container(
                    padding=padding.only(top=10, bottom=20),
                    content=categories_card  # Category cards
                ),
                Text("TODAY'S TASKS"),  # Section title for tasks
                Stack(
                    controls=[
                        tasks,  # List of tasks
                        FloatingActionButton(
                            icon=icons.ADD, on_click=lambda _: page.go('/create_task')  # Add task button
                        )
                    ]
                )
            ]
        )
    )

    # Container for the profile and menu page
    page_1 = Container(
        width=400,
        height=850,
        bgcolor=BG,
        border_radius=35,
        padding=padding.only(left=50, top=60, right=200),
        content=Column(
            controls=[
                Row(
                    controls=[
                        Container(border_radius=25,
                                  padding=padding.only(top=13, left=13),
                                  height=50,
                                  width=50,
                                  border=border.all(color='white', width=1),
                                  on_click=lambda e: undo_shrink(e),
                                  content=Text('<')  # Back button to undo shrink
                                  )
                    ]
                ),
                circle,  # Profile avatar
                Container(height=20),
                Text('Joe\nJackson', size=32, weight='bold'),  # User name
                Container(height=25),
                Row(controls=[
                    Icon(icons.FAVORITE_BORDER_SHARP, color='white12'),  # Favorite icon
                    Text('Templates', size=15, width=FontWeight.W_300, color='white', font_family='poppins')
                ]),
                Container(height=5),
                Row(controls=[
                    Icon(icons.CARD_TRAVEL, color='white12'),  # Categories icon
                    Text('Categories', size=15, width=FontWeight.W_300, color='white', font_family='poppins')
                ]),
                Container(height=5),
                Row(controls=[
                    Icon(icons.CALCULATE_OUTLINED, color='white12'),  # Analytics icon
                    Text('Analytics', size=15, width=FontWeight.W_300, color='white', font_family='poppins')
                ])
            ]
        )
    )

    # Container for the task management page (second page)
    page_2 = Row(alignment='end',
                 controls=[
                     Container(
                         width=400,
                         height=850,
                         bgcolor=FG,
                         border_radius=35,
                         animate=animation.Animation(600, AnimationCurve.EASE),
                         animate_scale=animation.Animation(400, AnimationCurve.DECELERATE),
                         padding=padding.only(top=50, left=20, right=20, bottom=5),
                         content=Column(
                             controls=[
                                 first_page_contents  # Main content on the second page
                             ]
                         )
                     )
                 ]
    )

    # Main container that holds both pages
    container = Container(
        width=400,
        height=850,
        bgcolor=BG,
        border_radius=35,
        content=Stack(
            controls=[
                page_1,  # Profile and menu page
                page_2   # Task management page
            ]
        )
    )

    # Define routes for navigation
    pages = {
        '/': View(
            "/",
            [
                container  # Default view
            ],
        ),
        '/create_task': View(
            "/create_task",
            [
                create_task_view  # View to create a task
            ],
        )
    }

    # Handle route changes to update the view
    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )

    page.add(container)  # Add the main container to the page
    page.on_route_change = route_change  # Set the route change handler
    page.go(page.route)  # Navigate to the current route

# Run the app
app(target=main)

Feature: A webapp is running

Scenario: webapp is running
        Given flaskr is set up
        When we hit the index
        Then the page shows the text "Índice"


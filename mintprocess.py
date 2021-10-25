import tools


def mint_process(stamp_data):
    tools.press_tab(1)
    tools.press_space(2)
    tools.paste_text("My NFT 1234")
    tools.press_return(1)


def mint_process(stamp_data):
    # Mint Process
    print("Minting: ", stamp_data["asset_title"])

    # INITIAL Process to start minting - CREATE BUTTON
    # - press tab 6x
    tools.press_tab(6)
    # - press enter 1x
    tools.press_return(1)
    tools.wait(2)
    tools.press_tab(6)

    # IMAGE UPLOAD
    # - press tab - 3x
    tools.press_tab(3)
    # - press enter - 1x
    tools.press_return(1)
    tools.wait(0.5)
    # - paste image_name
    tools.paste_text(stamp_data["image_name"])
    # - press enter 1x
    tools.press_return(1)
    tools.wait(2)

    # INSERT NAME
    # - press tab 1x
    tools.press_tab(2)
    # - insert asset_title
    tools.paste_text(stamp_data["asset_title"])

    # INSERT EXTERNAL URL
    # - press tab 1x
    tools.press_tab(1)
    # - insert external_url
    tools.paste_text(stamp_data["external_url"])
    tools.wait(0.5)

    # INSERT DESCRIPTION
    # - press tab 2x
    tools.press_tab(2)
    # - insert description
    tools.paste_text(stamp_data["description"])
    tools.wait(2)

    # SELECT COLLECTION
    # - press tab 1x
    tools.press_tab(1)
    # - wait 0.5 sec
    tools.wait(0.5)
    # - press tab 2x
    tools.press_tab(2)
    # - press return 1x
    tools.press_return(1)

    # CREATE PROPERTY
    # - press tab 1x
    tools.press_tab(1)
    # - press enter 1x
    tools.press_return(1)
    tools.wait(0.5)
    # - paste property
    tools.paste_text(stamp_data["property"])
    # - press tab 1x
    tools.press_tab(1)
    # - paste value
    tools.paste_text(stamp_data["value"])
    # - press tab 2x
    tools.press_tab(2)
    # - press enter
    tools.press_return(1)
    tools.wait(0.5)

    # SET UNLOCKABLE CONTENT
    # - press tab 3x
    tools.press_tab(4)
    # - press space 1x
    tools.press_space(1)
    tools.wait(0.5)
    # - press tab
    tools.press_tab(1)
    # - insert unlockable
    tools.paste_text(stamp_data["unlockable"])
    tools.wait(0.5)

    # SET BLOCKCHAIN
    # - press tab 4x
    tools.press_tab(4)
    # - press tab 1x
    tools.press_tab(1)
    # - press enter 1x
    tools.press_return(1)
    tools.wait(0.5)

    # SET SUPPLY
    # - press shift + tab
    tools.press_reverse_tab(2)
    # - insert max_supply
    tools.paste_text(stamp_data["max_supply"])

    # GO TO CREATE
    # - press tab 3x
    tools.press_tab(3)
    # - press enter
    tools.press_return(1)
    # - sleep 5 seconds
    tools.wait(5)
    tools.press_escape(1)
    tools.wait(0.2)
    tools.press_f5(1)
    tools.wait(3)

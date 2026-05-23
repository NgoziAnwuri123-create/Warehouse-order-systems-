import streamlit as st

st.title("Warehouse Order Processing System")

item_name = st.text_input("Enter Item Name")

item_cost = st.number_input(
    "Enter Item Cost",
    min_value=0.0
)

quantity = st.number_input(
    "Enter Quantity",
    min_value=1
)

if st.button("Calculate Total"):

    total = item_cost * quantity

    st.write(f"Order Total: £{round(total, 2)}")

    if total > 500:
        discounted_total = total * 0.9
    else:
        discounted_total = total

    st.write(
        f"Discounted Total: £{round(discounted_total, 2)}"
    )

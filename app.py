{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "820202f8-1207-4549-b0f3-17021c57cb76",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-05-23 13:42:20.749 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-05-23 13:42:21.621 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\CharlesQ\\AppData\\Local\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2026-05-23 13:42:21.622 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-05-23 13:42:21.623 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-05-23 13:42:21.625 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-05-23 13:42:21.627 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-05-23 13:42:21.628 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-05-23 13:42:21.629 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-05-23 13:42:21.630 Session state does not function when running a script without `streamlit run`\n",
      "2026-05-23 13:42:21.632 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-05-23 13:42:21.633 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-05-23 13:42:21.634 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-05-23 13:42:21.636 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-05-23 13:42:21.638 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-05-23 13:42:21.639 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-05-23 13:42:21.648 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-05-23 13:42:21.659 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-05-23 13:42:21.665 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-05-23 13:42:21.672 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-05-23 13:42:21.674 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-05-23 13:42:21.676 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-05-23 13:42:21.677 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-05-23 13:42:21.680 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-05-23 13:42:21.681 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-05-23 13:42:21.683 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-05-23 13:42:21.687 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-05-23 13:42:21.689 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-05-23 13:42:21.690 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-05-23 13:42:21.693 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-05-23 13:42:21.698 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-05-23 13:42:21.705 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-05-23 13:42:21.707 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "\n",
    "st.title(\"Warehouse Order Processing System\")\n",
    "\n",
    "item_name = st.text_input(\"Enter Item Name\")\n",
    "\n",
    "item_cost = st.number_input(\n",
    "    \"Enter Item Cost\",\n",
    "    min_value=0.0\n",
    ")\n",
    "\n",
    "quantity = st.number_input(\n",
    "    \"Enter Quantity\",\n",
    "    min_value=1\n",
    ")\n",
    "\n",
    "if st.button(\"Calculate\"):\n",
    "\n",
    "    total = item_cost * quantity\n",
    "\n",
    "    st.write(f\"Total Cost: £{total}\")\n",
    "\n",
    "    if total > 500:\n",
    "        discounted_total = total * 0.9\n",
    "    else:\n",
    "        discounted_total = total\n",
    "\n",
    "    st.write(\n",
    "        f\"Discounted Total: £{round(discounted_total, 2)}\"\n",
    "    )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bea886cc-4187-46c9-95fc-51c22947b43b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c2245292-776a-458e-9075-386bf977ebea",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9cfbf2df-518c-4c70-aeeb-316b2214651e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9c634a58-f45e-4612-a858-1e42f3d33640",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "829f64f6-df4b-467f-8eb6-2d4c9c1bec75",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b66b2cdd-045e-4a74-93bc-5699f1ff5fc3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

import axios from 'axios';
import {
  CART_ADD_ITEM,
  CART_REMOVE_ITEM,
} from '../constants/cartConstants';

const url = "http://127.0.0.1:8000/api/";

export const addToCart = (slug, qty) => async (dispatch, getState ) => {
  const { data } = await axios.get(`${url}products/${slug}`)

  dispatch({
    type:CART_ADD_ITEM,
    payload: {
      product: data.slug,
      name: data.name,
      image: data.image,
      property: data.property_fk,
      in_stock: data.in_stock,
      price: data.price,
      qty
    }
  })

  localStorage.setItem("cartItems", JSON.stringify(getState().cart.cartItems))

}
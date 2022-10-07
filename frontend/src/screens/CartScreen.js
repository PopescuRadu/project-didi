import React, { useEffect, useState } from 'react'

import { Link, useParams } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';

import { GoTriangleUp, GoTriangleDown } from 'react-icons/go';
import { FaTrash } from 'react-icons/fa';

import Message from '../components/message/Message';
import { addToCart } from '../actions/cartActions'

const CartScreen = () => {

  const decreaseQtyHandler = (e) => {
    if (e.value === 0) {
      e.value = 0
    } else {
      e.value = e.value - 1
    }
  }

  const params = useParams();
  const qty = params.qty ? Number(params.qty.split('=')[1]) : 1
  const slug = params.slug
  const dispatch = useDispatch();

  const cart = useSelector(state => state.cart)
  const { cartItems } = cart

  useEffect(() => {
    if(slug) {
      dispatch(addToCart(slug, qty))
    }
  }, [dispatch, slug, qty])

  const removeFromCartHandler = (slug) => {
    console.log("remove, ", slug)
  }

  return (
    <>
    {cartItems.length === 0 ? 
      <>
        <p> You didn't add items to you cart </p>
        <Link to="/catalogue"><button className='btn'>Browse Handmade Products</button></Link>
      </> 
      : 
        <div>
          {cartItems.map(item => (
            <div key={item.product}>
              <img src={item.image}  alt={item.name} />
              <Link to={`/catalogue/${item.product}`}>{item.name}</Link>
              <p>Price: {item.price}</p>
              <p>Quantity: {item.qty}</p>
              <p>Total: {item.qty * item.price}$</p>
              <button onClick={() => removeFromCartHandler(item.product)} className="btn btn-text">remove</button>
              <div className=''>
                <button value={item.qty} onClick={(e) => dispatch(addToCart(item.product, Number(e.target.value) + 1))}>{item.qty}<span><GoTriangleDown/></span></button>
                <p id="itemQty">Quantity: {item.qty}</p> 
                {/* asta de deasupra trebuie sa fie targetul. momentan, targetul la e.target este goTriangleDown  */}
                <button ><GoTriangleUp/></button>
            </div>
        </div>
          ))}
        </div>
    }
    
    </>
  )
}

export default CartScreen
import React, {useEffect, useState} from 'react';
import { useParams, useNavigate } from 'react-router-dom';

import Navbar from '../components/navbar/Navbar.jsx';

import {CgShoppingCart} from 'react-icons/cg';
import { GoTriangleUp, GoTriangleDown } from 'react-icons/go';

import { useDispatch, useSelector } from 'react-redux';

import Loader from '../components/loader/Loader'
import Message from '../components/message/Message'

import { listProductDetails } from '../actions/productActions';

const Product = () => {
  const {slug} = useParams();
  let navigate = useNavigate();

  const dispatch = useDispatch();
  const productDetails = useSelector(state => state.productDetails)

  const {loading, error, product} = productDetails

  const [qty, setQty ] = useState(1);

  useEffect(() => {
    dispatch(listProductDetails(slug))
  }, [dispatch]);

  const increaseQtyHandler = () => {
    setQty(qty + 1)
  }
  
  const decreaseQtyHandler = () => {
    if (qty <= 0) {
      qty = 0
    } else {
      setQty(qty - 1)
    }
  }

  const addToCartHandler = () => {
    navigate(`/cart/${slug}/qty=${qty}`)
  }

  return (
    
    <div>
      {loading ?
      <Loader/>
        : error
          ? <Message variant="danger">{error}</Message>
        :
        <>
          <Navbar />
          <h1>{product.name}</h1>
          <p>{product.description}</p>
          <button onClick={addToCartHandler}> add to cart <CgShoppingCart/> </button>
        </>
      } 

      <div>{product.in_stock === true 
        ? <>
            <p>Quantity: {qty}</p>
            <div className=''>
              <button onClick={decreaseQtyHandler}><GoTriangleDown/></button>
              <button onClick={increaseQtyHandler}><GoTriangleUp/></button>
            </div>
          </> 
        : 
          "sold out" 
        }</div>
    </div>
  )
}

export default Product
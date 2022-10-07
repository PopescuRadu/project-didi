import React, { useEffect } from 'react';
import { Link } from 'react-router-dom';

import { listProducts } from '../actions/productActions';
import Navbar from '../components/navbar/Navbar.jsx';

import Loader from '../components/loader/Loader.js';
import Message from '../components/message/Message.js';

import  {useDispatch, useSelector } from 'react-redux';

import { v4 as uuidv4 } from 'uuid';

const Products = () => {
  const productList = useSelector(state => state.productList)
  
  const {error, loading, products} = productList; 
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(listProducts())
  }, [dispatch]);

  return (
    <div>
      <h1>All Products</h1>
      <Navbar />
      { loading ? <Loader />
        : error ? <Message variant="danger">{error}</Message>
        :<>
            {products.map(product => (
            
              <div key={product.id}>
              <div/>
              
              <Link to={`/catalogue/${product.slug}`}>
                <h3>{product.name}</h3>
                <button>learn more</button>
              </Link>
              </div>
            ))}
          </>
    }
    </div>
  )
}

export default Products
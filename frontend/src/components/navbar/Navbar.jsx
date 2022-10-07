import React from 'react'
import { Link } from 'react-router-dom';

import { CgShoppingCart } from 'react-icons/cg';

const Navbar = () => {
  return (
    <nav className='navbar'>
      <Link className='navbar__link' to="/">home</Link>
      <Link className='navbar__link' to="/about">About</Link>
      <Link className='navbar__link' to="/catalogue">Catalogue</Link>
      <Link className='navbar__link' to="/cart">Cart <CgShoppingCart /> </Link>
      <Link className='navbar__link' to="/contact"><button> get in touch </button></Link>
    </nav>
  )
}

export default Navbar

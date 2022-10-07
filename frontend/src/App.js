
import ReactDOM from 'react-dom';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import 'bootstrap/dist/css/bootstrap.min.css';
import './main.css';
import './testing.scss';

import { About, Contact, Home, Products, Product, CartScreen } from './screens';

// for all pages, after some time, if customer device field is empty, create a new uuid code and save it to the customer database
// check cookies for existing code
// if code does not exist:
//   generate uuid code after delay
//   save uuid to new a new customer instance to db
// if code does exist:
//   break

function App() {
  return (
    <div>
      <BrowserRouter>
      <Routes>
          <Route path="/" element={<Home />} />
          <Route path="about" element={<About />} />
          <Route path="contact" element={<Contact />} />

          <Route exact path="catalogue" element={<Products />} />
          <Route path="catalogue/:slug" element={<Product />} />
          
          <Route path="cart" element={<CartScreen />}>
            <Route path=":slug" element={<CartScreen />}>
              <Route path=":qty" element={<CartScreen />} />
            </Route>
          </Route>

          {/* If no url paths are hit, this will show up */}
          <Route
            path="*"
            element={
              <main style={{ padding: "1rem" }}>
                <p>There's nothing here!</p>
              </main>
            }
          />

      </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;

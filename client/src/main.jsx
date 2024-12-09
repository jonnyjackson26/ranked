import React, { useState, useEffect, useContext } from 'react';
import ReactDOM from 'react-dom/client'
import Home from "./pages/Home/Home";
import { createHashRouter, RouterProvider } from 'react-router-dom'
import ProfilePage from './pages/ProfilePage/ProfilePage';
import StatsPage from './pages/StatsPage/StatsPage';


const router = createHashRouter([
  {
    path: "/",
    element: <Home />,
  },
  {
    path: "/profile",
    element: <ProfilePage />,
  },
  {
    path: "/stats",
    element: <StatsPage />,
  },
])


export const Context = React.createContext();

function Main() {


  return (
    <Context.Provider>
      <RouterProvider router={router} />
    </Context.Provider>
  )
}


ReactDOM.createRoot(document.getElementById('root')).render(
  <Main />
)
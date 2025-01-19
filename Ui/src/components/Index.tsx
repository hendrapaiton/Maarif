import React, { useEffect, useState } from "react";

const Index: React.FC<{ onLogout: () => void }> = ({ onLogout }) => {
  const [data, setData] = useState(null);

  const handleLogout = () => {
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    onLogout();
  };

  const fetchData = async () => {
    let token = localStorage.getItem("access");
    if (token) {
      try {
        let response = await fetch(
          "http://localhost:8000/api/protected-endpoint/",
          {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          }
        );

        if (response.status === 401) {
          const refreshToken = localStorage.getItem("refresh");
          if (refreshToken) {
            const refreshResponse = await fetch(
              "http://localhost:8000/api/token/refresh/",
              {
                method: "POST",
                headers: {
                  "Content-Type": "application/json",
                },
                body: JSON.stringify({ refresh: refreshToken }),
              }
            );

            if (refreshResponse.ok) {
              const refreshData = await refreshResponse.json();
              localStorage.setItem("access", refreshData.access);
              token = refreshData.access;

              response = await fetch(
                "http://localhost:8000/api/protected-endpoint/",
                {
                  headers: {
                    Authorization: `Bearer ${token}`,
                  },
                }
              );
            } else {
              handleLogout();
            }
          } else {
            handleLogout();
          }
        }

        if (response.ok) {
          const result = await response.json();
          setData(result.message);
        }
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div className="flex flex-col justify-center items-center h-screen">
      <h2 className="text-2xl font-bold uppercase">Protected Page</h2>
      <p className="text-sm text-gray-600">Welcome to the index page!</p>
      {data && (
        <p className="text-xs text-gray-400 mt-1">
          {JSON.stringify(data, null, 2)}
        </p>
      )}
      <button
        onClick={handleLogout}
        className="bg-red-600 text-white px-2 py-1 rounded-lg mt-4"
      >
        <i className="bi bi-door-closed me-3"></i>
        <span>Logout</span>
      </button>
    </div>
  );
};

export default Index;

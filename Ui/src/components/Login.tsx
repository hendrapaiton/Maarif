import React, { useState } from 'react';
import { login, LoginCredentials } from '../services/authService';

const Login: React.FC<{ onLogin: () => void }> = ({ onLogin }) => {
    const [username, setUsername] = useState<string>('');
    const [password, setPassword] = useState<string>('');

    const handleLogin = async () => {
        const credentials: LoginCredentials = { username, password };
        const success = await login(credentials);
        if (success) {
            onLogin();
        } else {
            alert('Invalid credentials');
        }
    };

    return (
        <div className="flex flex-col justify-center items-center h-screen">
            <h2 className="text-2xl font-bold mb-4 tracking-wider uppercase">Login Area</h2>
            <input
                type="text"
                placeholder="Username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                className="mb-2 p-2 border border-gray-300 rounded-lg w-64"
            />
            <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="mb-4 p-2 border border-gray-300 rounded-lg w-64"
            />
            <button
                onClick={handleLogin}
                className="bg-blue-600 text-white px-4 py-2 rounded-lg tracking-wide"
            >
                <i className="bi bi-door-open me-3"></i>
                <span>Login</span>
            </button>
        </div>
    );
};

export default Login;

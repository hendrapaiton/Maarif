export interface LoginCredentials {
    username: string;
    password: string;
}

export const login = async (credentials: LoginCredentials): Promise<boolean> => {
    try {
        const response = await fetch('http://localhost:8000/api/token/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(credentials),
        });

        if (response.ok) {
            const data = await response.json();
            localStorage.setItem('access', data.access);
            localStorage.setItem('refresh', data.refresh);
            return true;
        } else {
            return false;
        }
    } catch (error) {
        console.error('Login failed:', error);
        return false;
    }
};

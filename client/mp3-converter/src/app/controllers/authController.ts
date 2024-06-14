import { loginService } from "@/app/services/authService";

const login = async (username: string, password: string) => {
    const token = await loginService(username, password);
    console.log(token);
    console.log('To update cookies')
}

export {
    login,
}

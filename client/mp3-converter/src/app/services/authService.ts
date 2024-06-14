import { env } from '@/app/utils/env';

const loginService = async (username: String, password: String) => {
    const url = `${env.GATEWAY_URL}/api/auth/login`;
    const options = {
        method: 'POST',
        headers: {
            Authorization: `Basic ${Buffer.from(`${username}:${password}`).toString('base64')}`,
        },
    };
    const response = await fetch(url, options);
    const token =  await response.text();
    return token;
}

export {
    loginService,
}

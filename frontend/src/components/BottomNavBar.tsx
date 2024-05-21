import { Box, Typography } from '@mui/material';

const Footer = () => {
    return (
        <Box sx={{ bgcolor: '#000', color: '#fff', p: 2, width: '100%', mt: 'auto' }}>
            <Typography variant="body1" align="center">
                © 学生実験 2024
            </Typography>
        </Box>
    );
};

export default Footer;
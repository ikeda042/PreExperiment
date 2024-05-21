import { Box, Typography } from '@mui/material';

const Footer = () => {
    return (
        <Box sx={{ bgcolor: '#000', color: '#fff', mt: 3, p: 2, width: '100%' }}>
            <Typography variant="body1" align="center">
                © 学生実験 2023
            </Typography>
        </Box>
    );
};

export default Footer;
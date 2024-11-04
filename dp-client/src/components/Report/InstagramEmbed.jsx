import React, { useEffect } from 'react';

const InstagramEmbed = ({ postUrl }) => {
    useEffect(() => {
        // 인스타그램 임베드 스크립트를 다시 로드 (최신 게시물 표시를 위해)
        const script = document.createElement('script');
        script.async = true;
        script.src = '//www.instagram.com/embed.js';
        document.body.appendChild(script);
    }, [postUrl]);

    return (
        <div
            dangerouslySetInnerHTML={{
                __html: `
                <blockquote class="instagram-media" data-instgrm-permalink="${postUrl}" data-instgrm-version="14" style="max-width:540px; margin:auto;">
                    <a href="${postUrl}" target="_blank"></a>
                </blockquote>
                `,
            }}
        />
    );
};

export default InstagramEmbed;

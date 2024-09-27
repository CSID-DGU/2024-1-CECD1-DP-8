package com.cecd.dp.domain.influencer.dto;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class ProfileProjection {

    private String profilePictureUrl;
    private String nickname;
    private String name;
    private String category;
    private Integer mediaCnt;
    private Integer followerCnt;

    public ProfileProjection(String profilePictureUrl, String nickname, String name, String category, Integer mediaCnt, Integer followerCnt) {
        this.profilePictureUrl = profilePictureUrl;
        this.nickname = nickname;
        this.name = name;
        this.category = category;
        this.mediaCnt = mediaCnt;
        this.followerCnt = followerCnt;
    }
}

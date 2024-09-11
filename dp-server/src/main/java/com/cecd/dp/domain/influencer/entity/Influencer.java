package com.cecd.dp.domain.influencer.entity;

import com.cecd.dp.domain.media.entity.Media;
import com.cecd.dp.domain.meta.entity.Meta;
import com.cecd.dp.type.AccountType;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.hibernate.Hibernate;

import java.util.ArrayList;
import java.util.List;

@Entity
@NoArgsConstructor
@Getter
public class Influencer {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "influencer_id")
    private Long id;

    private String nickname; // 인스타 별명
    private String name; // 인스타 이름
    private String category; //  카테고리 종류가 다양해  Non-Enumerated
    private String graphId; // Insta GRAPH API 조회 ID
    private String email;
    @Enumerated(EnumType.STRING)
    private AccountType accountType;
    private String password;

    @Builder
    public Influencer(Long id, String nickname, String name, String category, String graphId, String email, AccountType accountType, String password) {
        this.id = id;
        this.nickname = nickname;
        this.name = name;
        this.category = category;
        this.graphId = graphId;
        this.email = email;
        this.accountType = accountType;
        this.password = password;
    }

    @OneToMany(mappedBy = "influencer", cascade = CascadeType.ALL)
    List<Media> mediaList = new ArrayList<>();

    @OneToMany(mappedBy = "influencer", cascade = CascadeType.ALL)
    List<Meta> metaList = new ArrayList<>();

    //===연관관계 편의 메서드===//
    public void addMedia(Media media) {
        if (mediaList.contains(media)) {
            mediaList.remove(media);
        }
        media.setInfluencer(this);
        this.mediaList.add(media);
    }

    public void addMeta(Meta meta) {
        if (metaList.contains(meta)) {
            metaList.remove(meta);
        }
        meta.setInfluencer(this);
        this.metaList.add(meta);
    }

    //===보조 메서드===//
    public Meta getLatestMeta() {
        return metaList.get(metaList.size() - 1);
    }

    public Integer getMediaCnt() {
        return mediaList.size();
    }
}

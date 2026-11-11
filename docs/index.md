title: 涓婚〉

# [妯℃嫙鍣ㄧ殑 ROS 鏂囨。](https://github.com/OpenHUTB/ros2)

娆㈣繋浣跨敤 OpenHUTB 鐨?ROS 鏂囨。 [@macenski2022robot]銆?
鏂囨。鐜鍒濆鍖栵細[Ubuntu 涓€閿畨瑁呬笌鏈湴棰勮](./ubuntu_docs_setup.md)銆?
<span id="submission-guide"></span>
**鎻愪氦椤圭洰涔嬪墠**锛岃鎸変互涓嬫寚寮曡嚜鏌ワ紝骞堕槄璇籟浠撳簱鎻愪氦绾﹀畾](https://github.com/OpenHUTB/ros2#娉ㄦ剰浜嬮」)銆侾R 妯℃澘鍙垪甯歌妫€鏌ラ」锛涘叿浣撲换鍔°€佹ā鎷熷櫒鍜岄獙鏀惰姹備互浠撳簱绾﹀畾鍙婄淮鎶よ€呰鏄庝负鍑嗐€?
<details>
<summary>灞曞紑椤圭洰鎻愪氦涓庡鐜版寚寮?/summary>

<ol>
<li><strong>纭鎻愪氦鑼冨洿銆?/strong> 鍦?Files changed 涓€愪釜妫€鏌ユ柊澧炪€佷慨鏀瑰拰鍒犻櫎銆備笉瑕佹彁浜?build銆乮nstall銆乴og 绛夋棤鍏崇敓鎴愮洰褰曘€佸浠芥垨閲嶅鏂囦欢锛屼笉鐢ㄤ釜浜洪」鐩唴瀹硅鐩栦粨搴撻椤靛強鍏叡閰嶇疆銆傞渶瑕佷慨鏀瑰叕鍏卞唴瀹规椂璇存槑鍘熷洜涓庡奖鍝嶃€?/li>
<li><strong>鏁寸悊妯″潡涓庡惎鍔ㄥ叆鍙ｃ€?/strong> 婧愮爜鏀惧湪 src 瀵瑰簲妯″潡锛屾暀绋嬫斁鍦?docs 瀵瑰簲妯″潡锛屾枃浠朵娇鐢ㄨ嫳鏂囦笅鍒掔嚎鍛藉悕銆傛彁渚?main.* 鍜?launch锛屾牳瀵瑰寘鍚嶃€佸彲鎵ц鍚嶃€佷緷璧栥€佹ā鍨嬭矾寰勫強瀹夎瑙勫垯锛屽畬鍠勫疄闄呭寘鎻忚堪銆佺淮鎶や俊鎭拰璁稿彲璇併€?/li>
<li><strong>鎸夋枃妗ｅ畬鏁磋繍琛屻€?/strong> README 鍐欐竻瀹為檯楠岃瘉鐨勭郴缁熴€丷OS銆丳ython銆佹ā鎷熷櫒鍜屽叧閿緷璧栫増鏈紝浠ュ強鑾峰彇婧愮爜銆佸畨瑁呫€佹瀯寤恒€佸姞杞界幆澧冦€佸惎鍔ㄥ拰鍋滄姝ラ锛屾敞鏄庢墽琛岀洰褰曘€傚缓璁粠鏂扮粓绔搷浣滐紝妫€鏌ラ敭鐩樿緭鍏ャ€佽繍鍔ㄦ柟鍚戙€佺姸鎬佸垏鎹€侀€€鍑哄仠杞﹀拰寮傚父娓呯悊銆?/li>
<li><strong>鍑嗙‘璇存槑楠岃瘉鑼冨洿銆?/strong> 鍖哄垎鑺傜偣鍚姩銆佽瘽棰橀€氫俊銆佸彲瑙嗗寲婕旂ず涓庡畬鏁翠豢鐪熸晥鏋溿€傚浐瀹氶€熷害鍙戝竷涓嶇瓑浜庤建杩硅窡韪紝绂荤嚎娴嬭瘯涓嶇瓑浜庡湪绾块棴鐜獙璇併€傛寚鏍囨敞鏄庡畾涔夈€佸崟浣嶃€佸満鏅笌娴嬮噺鏂规硶锛屼繚鐣欏繀瑕佹棩蹇楋紱鏈獙璇佺殑鍐呭鍜岀畝鍖栧亣璁惧瀹炶鏄庛€?/li>
<li><strong>妫€鏌ョ綉椤典笌閰嶅浘銆?/strong> 鏂版ā鍧楀湪鏈椤靛拰 mkdocs.yml 澧炲姞鍏ュ彛锛岃繍琛?<code>mkdocs serve --livereload</code> 妫€鏌ョ浉鍏抽〉闈€侀摼鎺ャ€佸叕寮忓拰娴佺▼鍥俱€備娇鐢ㄧ湡瀹炶繍琛屾埅鍥捐€岄潪鎷嶇収锛岀ず鎰忓浘鏄庣‘鏍囨敞锛汸NG 灏忎簬 3 MB銆丟IF 灏忎簬 5 MB锛屽ぇ閲忔暟鎹彁渚涙寔涔呬笅杞介摼鎺ャ€?/li>
<li><strong>瀹屾垚璇存槑涓庡鏍搞€?/strong> PR 鏍囬鍜屾彁浜や俊鎭鏄庝慨鏀圭洰鐨勶紝浣跨敤澶фā鍨嬫椂澹版槑鍏蜂綋宸ュ叿骞跺鍐呭璐熻矗銆傚悎骞跺墠鑷冲皯涓€鍚嶅叾浠栦汉鍦ㄥ彟涓€鍙版満鍣ㄦ祴璇曞苟鍚屾剰锛屼笉鑳界敤浣滆€呰嚜娴嬫浛浠ｃ€傜函鏂囨。鎴栧眬閮ㄤ慨澶嶆寜瀹為檯褰卞搷妫€鏌ワ紝涓嶈姹傛柊澧炴棤鍏虫ā鍧椼€?/li>
</ol>
<p>浠ヤ笂缁撳悎浠撳簱瑕佹眰鍜屽鐜板缓璁暣鐞嗭紝涓嶄綔涓烘柊澧炶瘎鍒嗘爣鍑嗐€備篃鍙弬闃?a href="https://github.com/OpenHUTB/doc#鎾板啓瑙勮寖">鏂囨。鎾板啓绾﹀畾</a>鍜?a href="https://github.com/OpenHUTB/.github/blob/master/CONTRIBUTING.md">璐＄尞鎸囧崡</a>銆?/p>

</details>

- [绠€浠媇(#list)
  - [鍏ラ棬](#list)
  - [浜哄舰鏈哄櫒浜篯(#humanoid)
  - [鑲岃倝楠ㄩ浜篯(#musculoskeletal)
  - [鍦伴潰杞藉叿](#ground_vehicle)
  - [绌哄煙杞藉叿](#air_vehicle)
  - [姘村煙杞藉叿](#water_vehicle)

---

## 1. 鍏ラ棬 <span id="list"></span>

ROS 鐩稿叧璧勬枡锛圼缃戠洏涓嬭浇鍦板潃](https://pan.baidu.com/s/1viua4SZ7tP2DtU2XlCRKPg?pwd=hutb)锛夛細

* 鏁欐潗锛歊OS鏁欐潗.pdf
* 璇句欢鍜岃棰戯細ROS璧勬枡.zip
* 瀹夎濂?ros kinetic 鐨勮櫄鎷熸満锛堝瘑鐮侊細rosindustrial锛塙buntu 16.04锛?.ova
* Windows铏氭嫙鏈猴紙瀵嗛挜锛歓F3R0-FHED2-M80TY-8QYGC-NPKYF锛夛細*.exe
* 琛ュ厖锛歔ubuntu涓嬭櫄鎷熸満鐨勮繍琛屾柟寮廬(ubuntu涓嬭櫄鎷熸満鐨勮繍琛屾柟寮?md)
* [铏氭嫙鏈虹幆澧冧粙缁峕(./vm_introduction.md)
* 琛ュ厖锛歔Ubuntu 20.04 瀹夎 ROS Noetic 璇︾粏鏁欑▼](ubuntu20.04.md)

[涓嬭浇](https://ww2.mathworks.cn/support/product/robotics/ros2-vm-installation-instructions-v9.html)骞跺畨瑁呭ソ ROS 鐨勮櫄鎷熸満銆傛铏氭嫙鏈哄熀浜?Linux 锛圲buntu 20.04 `lsb_release -a`锛夋搷浣滅郴缁燂紝骞跺凡棰勫厛閰嶇疆涓烘敮鎸佷娇鐢?ROS 锛圧OS 1 Noetic 鍜?ROS 2 Humble锛?鏋勫缓鐨勫簲鐢ㄧ▼搴忋€?

ROS姣忕珷鑺傝繍琛屼唬鐮?

* [绗?1 绔燷(./chapter/chap1/chap1.md) - 璁よ瘑 ROS
* [绗?2 绔燷(./chapter/chap2.md) - ROS 鍩虹
    * [ROS 2 璇濋鍙戝竷璁㈤槄鍩虹瀹為獙锛坱alker/listener锛塢(./chap2/ros2_pubsub_py.md)
    * [ROS Noetic 澶氫紶鎰熷櫒璇濋鏃堕棿鍚屾](./chap2/ros1_message_time_sync/index.md)
    * [ROS Noetic 杩愯鍙傛暟鐑洿鏂帮紙姝ｅ鸡淇″彿锛塢(./chap2/ros1_parameter_sine_wave/index.md)
    * [ROS Noetic 鐜鑷涓庡父瑙侀棶棰樻帓鏌(./chap2/ros1_env_check/index.md)
    * [ROS 2 浼犳劅鍣ㄦ暟鎹潎鍊兼护娉㈣妭鐐?(mean_filter)](./chap2/mean_filter.md)
* [绗?3 绔燷(./chapter/chap3.md) - 鏈哄櫒浜虹郴缁熻璁?* [绗?4 绔燷(./chapter/chap4.md) - 鏈哄櫒浜轰豢鐪?    * [URDF 鍥涜疆灏忚溅寤烘ā涓?RViz 鏄剧ず](./chapter/urdf_car_modeling.md)
* [绗?5 绔燷(./chapter/chap5.md) - 鏈哄櫒浜烘劅鐭?    * [琛屼汉闅愮鑴辨晱瑙嗚妫€娴嬭妭鐐筣(./privacy_mask/README.md)
* [绗?6 绔燷(./chapter/chap6.md) - 鏈哄櫒浜?SLAM 涓庤嚜涓诲鑸?    * [鑷缓灏忚溅 Gazebo GMapping 寤哄浘](./chapter/urdf_car_gmapping.md)
* [绗?7 绔燷(./chapter/chap7.md) - 闃垮厠鏇煎洓杞皬杞﹁繍鍔ㄦ帶鍒?* [绗?8 绔燷(./chapter/chap8.md) - ROS 鏈哄櫒浜虹患鍚堝簲鐢?    * [鏈哄櫒瑙嗚澶氭満鍣ㄤ汉铓佺兢缂栭槦](./ant/README.md)
    * [PocketSphinx 璇煶鎺у埗灏忎箤榫焆(./voice/pocketsphinx_noetic.md)
    * [MoveIt 鍏嚜鐢卞害鏈烘鑷傝繍鍔ㄨ鍒抅(./chapter/chap8/moveit_arm_planning.md)
    * [鏈烘鑷傛嫥铻轰笣浠跨湡](./chapter/chap8/mujoco_arm_screw.md)
    * [MuJoCo UR5e 鍏宠妭绌洪棿鎶撴斁鎺у埗](./chapter/ur5e_pickplace.md)
    * [MuJoCo 浜岃繛鏉嗙瑳鍗″皵闃绘姉鍔涙帶](./chapter/two_link_impedance_control.md)
    * [鏈烘鑷傛姇绡叆绛愪豢鐪焆(./chapter/mujoco_arm_ball.md)
    * [MuJoCo 浜岃繛鏉嗘満姊拌噦鎶撳彇鎼繍](./chapter/mujoco_arm_pick.md)
    * [涓夎嚜鐢卞害鏈烘鑷傜┖闂磋灪鏃嬬嚎浠跨湡](./chapter/mujoco_arm_3d.md)
    * [MuJoCo 鍙岃嚜鐢卞害鏈烘鑷傜敾姝ｆ柟褰(./chapter/mujoco_two_dof_arm_square.md)
    * [MuJoCo 浜岃繛鏉嗘満姊拌噦 IK 鐢诲渾](./chapter/mujoco_arm_ik.md)
* [绗?9 绔燷(./chapter/chap9.md) - ROS 2
* [绗?10 绔燷(./chapter/turtlebot3_gazebo_control.md) - Turtlebot3 Gazebo閿洏鎺у埗


ROS 2 鏈嶅姟涓庡弬鏁板熀纭€瀹為獙锛堟棤浜烘満妯″紡鍒囨崲涓庡湪绾胯皟鍙傦級锛歔chap2/ros2_service_param_demo](./chap2/ros2_service_param_demo.md)

## 2. 浜哄舰鏈哄櫒浜?<span id='humanoid'></span>

* [浜哄舰鏈哄櫒浜哄熀纭€](./humanoid/humanoid_basics.md)
* [浜哄舰鏈哄櫒浜哄弻鑷傛惉杩愯礋杞界殑绁炵粡缃戠粶骞宠　鎺у埗](./humanoid/humanoid_carry_payload_nn.md)
* [鍙岃冻姝ユ€佺敓鎴愪笌 ZMP 绋冲畾鎬(./humanoid/bipedal_gait_zmp.md)
* [鍩轰簬涓夋鏍锋潯鎻掑€肩殑鍙岃冻澶氭鎬佸钩婊戝垏鎹(./humanoid/biped_cubic_spline_gait_switch.md)
* [浜哄舰鏈哄櫒浜洪敭鐩樿繍鍔ㄦ帶鍒禲(./humanoid/humanoid_keyboard_control.md)
* [浜哄舰鏈哄櫒浜哄钩琛℃帶鍒朵笌澶栧姏鎶楁壈鎭㈠](./humanoid/humanoid_push_recovery.md)
* [浜哄舰鏈哄櫒浜?PPO 绁炵粡缃戠粶骞宠　鎺у埗](./humanoid/humanoid_ppo_locomotion.md)
* [浜哄舰鏈哄櫒浜?2D 婵€鍏夐浄杈?CNN 鎰熺煡涓庨伩闅淽(./humanoid/humanoid_lidar_nn_perception.md)
* [浜哄舰瓒宠抗涓嬬殑灞€閮ㄩ伩闅滅畻娉曞姣擼(./humanoid/humanoid_local_planner_bench.md)
* [MuJoCo鍗曡冻寮硅烦鏈哄櫒浜虹畝鍗曚豢鐪焆(./humanoid/mujoco_hopper_demo/index.md)
* [浜哄舰鏈哄櫒浜哄叧鑺傝建杩瑰綍鍒朵笌鍥炴斁宸ュ叿](./humanoid/humanoid_joint_tools.md)
* [浜哄舰涓婁笅鍙伴樁姝ユ€佷豢鐪焆(./humanoid/humanoid_stair_climb.md)
* [ROS铏氭嫙鏈哄櫒浜哄渾褰㈣建杩箁viz鍙鍖栫ず渚媇(./humanoid/ros_topic_demo/index.md)
* [浜哄舰鏈哄櫒浜哄叏韬€嗚繍鍔ㄥ涓庡彲鎿嶄綔鎬(./humanoid/whole_body_ik.md)
* [浜哄舰鏈哄櫒浜哄弻鑷傛湯绔彲杈惧煙鍒嗘瀽](./humanoid/humanoid_reachability.md)
* [浜哄舰鏈哄櫒浜鸿穼鍊掗鍒や笌淇濇姢鎬у€掑湴](./humanoid/humanoid_fall_protection.md)
* [浜哄舰鏈哄櫒浜?3D 纰版挒浣撹竟鐣屾娴嬪彲瑙嗗寲](./humanoid/humanoid_collision_boundary.md)
*  [绠€鍖栧弻瓒虫鎬佸姩鐢绘紨绀篯(./humanoid/zmp_walk_planner.md)
* [浜哄舰鏈哄櫒浜鸿交閲忕骇 ZMP 姝ヨ鎺у埗鍩虹嚎](./humanoid/humanoid_zmp_walking.md)
* [浜哄舰鏈哄櫒浜烘繁搴﹀浘濮挎€佷及璁′笌骞宠　鎺у埗](./humanoid/humanoid_depth_pose_control.md)
* [鍏宠妭鎸囦护鐨?QoS 涓庢椂寤跺奖鍝嶈瘎浼癩(./humanoid/joint_qos_latency_eval.md)
* [浜哄舰鏈哄櫒浜?IMU 濮挎€佽В绠楋細浜掕ˉ婊ゆ尝涓?Madgwick 瀵规瘮](./humanoid/humanoid_imu_attitude.md)
* [浜哄舰鏈哄櫒浜虹绾胯闊虫寚浠ゆ帶鍒禲(./humanoid/humanoid_voice_command.md)
* [浜哄舰鏈哄櫒浜鸿窇姝ョ墰椤跨浜屽畾寰嬬悊璁鸿绠椾笌婕旂ず](./humanoid/humanoid_newton_running.md)
* [浜哄舰鏈哄櫒浜哄叏韬煍椤烘帶鍒禲(./humanoid/humanoid_g1_compliance.md)


## 3. 鑲岃倝楠ㄩ浜?<span id='musculoskeletal'></span>

* [鑲岃倝楠ㄩ浜哄熀纭€](./musculoskeletal/musculoskeletal_basics.md)
* [鑲岃倝-鑲岃叡涓茶仈寮规€у疄楠宂(./musculoskeletal/msk_tendon_basics.md) 鈥斺€?鍗曞叧鑺?+ 鎷姉鑲岋紝鑲岃叡鍌ㄨ兘/浼犲姏/閲婃斁涓夌粍瀹為獙
* [MuJoCo鑲岃倝楠ㄩ浜洪敭鐩橀仴鎿嶄綔琛岃蛋韪㈣吙韫茶捣](./musculoskeletal/msk_human_walking_teleop.md) 鈥斺€?22 鏉?Hill 鑲岃倝椹卞姩 13 DoF 鍏ㄨ韩妯″瀷锛屽钩鍦?鍧￠亾/璐熻浇涓夊満鏅?* [MuJoCo 鑲岃倝楠ㄩ鐏靛阀鎵嬶細閿洏閬ユ搷浣滀笌绁炵粡缃戠粶鑲岃倝婵€娲绘帶鍒禲(./musculoskeletal/msk_hand_teleop.md)
* [MuJoCo 鍙屽叧鑺傝倢鑲夐楠兼墜鑷傚埌杈炬帶鍒禲(./musculoskeletal/msk_arm_reach.md)
* [MuJoCo 鑲岃倝楠ㄩ鎵嬭噦鏈綋鎰熻涓庝覆鑱斿脊鎬ц倢鑵盷(./musculoskeletal/msk_arm_proprioception.md)
* [鑲岃倝椹卞姩鐨勫叧鑺傛帶鍒朵笌 Hill 鑲岃倝妯″瀷](./musculoskeletal/muscle_joint_control.md)
* [鑲岃倝鐤插姵寤烘ā锛氭寔缁敹缂╀笅鐨勮倢鍔涜“鍑忎笌鎭㈠](./musculoskeletal/muscle_fatigue.md) 鈥斺€?鍦?Hill 妯″瀷涓婂彔鍔犵柌鍔冲洜瀛愶紝瀵规瘮鎸佺画涓庨棿姝囨敹缂╃殑鍔涜“鍑?* [鑲岃倝椹卞姩鐨勫す鐖姄鍙栵細鐪熷疄鎺ヨЕ鎶撳彇](./musculoskeletal/msk_gripper.md)
* [鑲岃倝椹卞姩鐨勪笅鑲㈠叧鑺備笌姝ユ€乚(./musculoskeletal/muscle_leg_gait.md)
* [鑶濆叧鑺傝倢鑲夐楠间豢鐪熶笌杞ㄨ抗璺熻釜](./musculoskeletal/knee_tracking.md)
* [鏈烘鑷傛墜鐪兼爣瀹氫豢鐪焆(./humanoid/hand_eye_calibration.md) 

## 4. 鍦伴潰杞藉叿  <span id='ground_vehicle'></span>
* [缂栫爜鍣ㄩ噺鍖栬宸笌閫熷害浼拌婊ゆ尝瀵规瘮](./ground/encoder_quantization_velocity.md) 鈥斺€?1 kHz 宸垎鎶婇噺鍖栬宸斁澶у崈鍊嶏紱1024/4096/16384 CPR 涓嬪師濮嬪樊鍒?1.371鈫?.404鈫?.133 rad/s锛屛?尾 涓庡崱灏旀浖鎶婅宸帇鍒?0.198/0.047
* [姣背娉㈤浄杈剧洰鏍囪窡韪笌鍓嶇鎾為璀︼紙TTC/FCW锛塢(./ground/radar_ttc_fcw.md) 鈥斺€?鐢ㄥ鏅嫆閫熷害鍒嗙闈欐鏉傛尝锛屽甯у叧鑱斾及璁?TTC 骞惰緭鍑?SAFE/WARN/STOP 鍒嗙骇棰勮
 - [鍩轰簬 1D CNN 鐨勬縺鍏夐浄杈?SLAM](./ground/carla_nn_scan_matching.md)

* [鎵嬪姩鎺у埗](./set_up_and_connect_to_carla.md)
* [MNIST 鎵嬪啓鏁板瓧瑙嗚鎰熺煡涓庢満鍣ㄤ汉杩愬姩鎺у埗](./ground/mnist_digit_control.md) 鈥斺€?CNN 璇嗗埆鎵嬪啓鏁板瓧涓鸿繍鍔ㄦ寚浠わ紝闃叉姈纭鍚庢帶鍒?turtlesim 骞崇Щ/鏃嬭浆
* [鐢熸垚瀵硅薄](./ground/carla_spawn_objects.md)
* [鍦伴潰杞藉叿鐗╃悊浠跨湡涓庨敭鐩樿繍鍔ㄦ帶鍒禲(./ground/carla_keyboard_control.md)
* [CARLA+YOLOv8 鐩爣妫€娴嬫劅鐭ヤ笌鍑忛€熼伩闅淽(./ground/carla_yolo_avoidance.md)
* [闃垮厠鏇兼帶鍒禲(./ground/ackermann_control.md)
* [杞﹂亾绾挎娴嬶紙鍓嶈瑙嗚锛塢(./ground/carla_lane_keeping/lane_detection.md)
* [杞﹂亾淇濇寔鎺у埗](./ground/carla_lane_keeping/lane_keeping_control.md)
* [浼犳劅鍣ㄦ劅鐭ヤ笌缁欏畾杞ㄨ抗璺熻釜锛堢缁忕綉缁滅増锛塢(./ground/carla_perception_control.md)
* [R2D2灏忚溅鑷姩宸¤埅浠跨湡](./ground/r2d2_cruise.md)
* [R2D2灏忚溅鑸偣宸¤埅浠跨湡](./ground/r2d2_waypoint_cruise.md) 鈥斺€?P鎺у埗鍣ㄨ埅鐐硅窡韪紝鏂瑰舰璺緞寰幆宸￠€伙紝闄勮建杩规暟鎹褰?* [璺緞鐐瑰彂甯冨櫒](./ground/waypoint.md)
* [婵€鍏夐浄杈惧缓鍥句笌绁炵粡缃戠粶瑙勫垝瀵艰埅](./ground/carla_mapping_navigation.md)
* [鑷姩椹鹃┒浠ｇ悊](./ground/ad_agent.md)
* [绔埌绔缁忕綉缁滃浘鍍忛┚椹禲(./ground/carla_end_to_end_nn.md)
* [鐜矝姹囧叆绔埌绔┚椹讹紙鍥惧儚鈫掓帶鍒讹級](./ground/carla_nn_roundabout_entry.md)
* [鑷姩椹鹃┒绀轰緥](./ground/ad_demo.md)
* [rostopic 鎵嬪姩椹卞姩](./ground/rostopic_cruise.md)
* [浣滀笟缁煎悎鏁村悎涓庢€ц兘璇勪环](./ground/carla_benchmark_suite.md)
* [ROS Scenario Runner](./ground/ros_scenario_runner.md)
* [浜ら€氫俊鍙风伅璇嗗埆涓庡搷搴擼(./ground/carla_traffic_light.md)
* [RVIZ Carla 鎻掍欢](./ground/rviz_plugin.md)
* [鎵浆鎺у埗](./ground/twist_to_control.md)
* [鎹㈤亾鍙鎬у垽瀹歖(./ground/lane_change_feasibility.md)
* [鍊掕溅闆疯揪鍒嗙骇鍛婅](./ground/ultrasonic_rear_alert.md)
* [閲岀▼璁¤建杩硅褰昡(./ground/odom_trace_recorder.md)
* [杞悜鎵ц鍣ㄦ粸鍚嶿(./ground/steering_actuator_lag.md)
* [鍒硅溅璺濈鏍哥畻](./ground/braking_distance_check.md)
* [鎹㈡尅绛栫暐涓庨棴鐜帶鍒禲(./ground/gear_shift_policy.md)
* [鐗靛紩杞︽寕杞︽姌鍒€鍒ゅ畾](./ground/trailer_kinematics.md)
* [閫熷害鏇茬嚎瑙勫垝](./ground/speed_profile_check.md)
* [杞集鎵帬鏍￠獙](./ground/turning_sweep_check.md)
* [RQT 鎻掍欢](./ground/rqt_plugin.md)
* [婵€鍏夐浄杈剧偣浜戣涔夊垎鍓瞉(./ground/carla_lidar_pointcloud_segmentation.md)
* [鐐逛簯鍦板浘鍒涘缓](./ground/pcl_recorder.md)
* [瀹氱偣鍋滆溅](./ground/fixed_point_stop.md)
* [ROS涓嶤onda鐜鎺掗敊鎸囧崡](./ground/ros_conda_env_guide.md)
* [鎵撻澏](./ground/mujoco_shooting.md)
* [Carla 浜ら€氭爣蹇楄瘑鍒紙Windows 鑴氭湰锛塢(./ground/carla_traffic_sign_recognition.md) - 鍩轰簬 YOLOv8 鐨勫疄鏃舵劅鐭ヤ笌閿洏鎺у埗

* [YOLOv8 瑙嗚鎰熺煡鐩爣璺熼殢浠跨湡](./ground/yolov8_target_tracking.md)
* [杞﹁締閿洏閬ユ搷浣滀笌浜岀淮妯℃嫙](./ground/vehicle_pygame_teleop.md)

* [浠诲姟1锛氭満鍣ㄤ汉閿洏鎺у埗妯″潡](./robot_tasks/teleop_control/README.md)
* [浠诲姟2: 妯℃嫙浼犳劅鍣ㄦ暟鎹簮](./robot_tasks/sensor_perception/README.md)
* [浠诲姟3: 瀵艰埅涓庤矾寰勮鍒掓ā鍧梋(./robot_tasks/navigation_slam/README.md)
* [浠诲姟4锛氱鍒扮绛栫暐缃戠粶](./robot_tasks/policy_learning/README.md)

* [TurtleBot3 婵€鍏夐浄杈捐嚜涓婚伩闅滐紙ROS 2锛塢(./ground/turtlebot3_lidar_avoid.md) 鈥斺€?璁㈤槄鏈鸿浇婵€鍏夐浄杈撅紝鎸夋墖鍖烘彁鍙栧墠/宸?鍙虫渶杩戣窛绂伙紝缁忎笁鎬佺姸鎬佹満涓庡娍鍦烘硶鍐崇瓥鍚庡彂甯?/cmd_vel锛屽疄鐜拌糠瀹満鏅嚜涓婚伩闅?* [Mbot 闆疯揪閬块殰浠跨湡锛圧OS 1 Noetic锛塢(./ground/mbot_lidar_avoid.md) 鈥斺€?Mbot 宸€熷簳鐩樺湪 Gazebo 涓殑 2D 婵€鍏夐浄杈鹃槇鍊奸伩闅滐紝鎸夋墖鍖烘渶灏忚窛绂?+ 婊炲洖鐘舵€佹満杈撳嚭 /cmd_vel

* [缃戦〉杩滅▼閬ユ帶灏忚溅](./ground/web_remote_car.md)
* [MuJoCo AEB鑷姩绱ф€ュ埗鍔ㄤ豢鐪焆(./ground/mujoco_vehicle_aeb.md)
* [绔埌绔┚椹讹紙鍥惧儚鍒版帶鍒舵寚浠わ級](./ground/pix2cmd_end2end_driving.md)

* [MuJoCo 宸€熷皬杞﹁疆婊戞劅鐭ヤ笌杞ㄨ抗琛ュ伩](./ground/mujoco_diff_drive_slip_compensation.md)
* [MuJoCo 鍦伴潰灏忚溅灏勭嚎鎰熺煡涓庡垎绾у噺閫熼伩闅淽(./ground/mujoco_car_avoidance.md)
* [MuJoCo 鍦伴潰灏忚溅绁炵粡缃戠粶绔埌绔伩闅淽(./ground/mujoco_car_nn_avoidance.md)
* [MuJoCo 涓よ疆鑷钩琛″皬杞(./ground/mujoco_balance_car.md)
* [MuJoCo 鍦伴潰宸€熷皬杞︿晶鍊?缈昏溅椋庨櫓棰勬祴涓庝富鍔ㄩ檺閫焆(./ground/mujoco_car_rollover_guard.md)
* [MuJoCo 鍦伴潰宸€熷皬杞﹀崟渚ч┍鍔ㄥけ鏁堟娴嬩笌宸€熻ˉ鍋縘(./ground/mujoco_car_drive_fault.md)
* [2D 灏忚溅鐩爣杩借釜浠跨湡](./ground/car_2d_target_tracker.md)
* [鍩轰簬绁炵粡缃戠粶鐨勬棤浜哄皬杞﹁嚜閫傚簲璺熻溅锛圓CC锛塢(./ground/carla_nn_car_following.md)
* [Gazebo 宸€熷皬杞﹂敭鐩樻帶鍒禲(./ground/gazebo_diff_drive_teleop.md)
* [鎭跺姡闆ㄩ浘澶╂皵涓嬪浼犳劅鍣ㄦ劅鐭ユ€ц兘瀵规瘮瀹為獙](./ground/weather_perception_benchmark.md)
* [绁炵粡缃戠粶寮哄寲瀛︿範绠楁硶涓庣綉缁滅粨鏋勫姣旓紙MuJoCo CartPole锛塢(./ground/rl_algorithm_compare.md)
* [鍩轰簬Mujoco鐨勯敭鐩橀仴鎺у皬杞(./ground/mujoco_car_project.md)
* [鍦伴潰杞藉叿妯悜鎺у埗绠楁硶瀵规瘮锛堢函璺熻釜 / Stanley / LQR锛塢(./ground/lateral_control_benchmark.md) 鈥斺€?鍚屼竴杞﹁締妯″瀷涓庢寚鏍囦笅瀹氶噺姣旇緝涓夌妯悜鎺у埗鍣?* [ROS2 宸€熸満鍣ㄤ汉 A* 鍏ㄥ眬瑙勫垝涓?DWA 灞€閮ㄩ伩闅淽(./ground/ros2_dwa_avoidance.md)
* [ROS2 DWA 灞€閮ㄨ鍒掑櫒闅忔満鍦烘櫙鍘嬪姏娴嬭瘯涓庤垝閫傛€ц瘎浠穄(./ground/ros2_dwa_benchmark.md)
* [ROS2 A*+DWA 鐨?Gazebo 涓夌淮楠岃瘉](./ground/ros2_dwa_gazebo.md)
* [TurtleBot3 浠跨湡鑷富瀵艰埅涓庨伩闅滃弬鏁颁紭鍖朷(./ground/turtlebot3_auto_nav/README.md)
* [鍦伴潰鏃犱汉杞﹁瑙?SLAM 寤哄浘涓庤嚜涓诲鑸猐(./ground/ugv_visual_slam_nav.md) 鈥斺€?鍗曠洰 RGB-D 鍋?EKF-SLAM 涓庡崰鎹爡鏍硷紝A\* 瑙勫垝 + 绾拷韪墽琛岋紝骞舵帓璁粌绔埌绔?CNN 鍋氬鐓?* [MuJoCo Locomotion 寮哄寲瀛︿範瀵规瘮瀹為獙](./ground/rl_mujoco_locomotion.md)
* [鍥惧儚褰曞埗 ROS 2 灏佽妯″潡](./ground/image_recorder.md)
* [MuJoCo灏忚溅鍊掕溅鍏ュ簱浠跨湡](./ground/mujoco_car_parking.md)
* [MuJoCo 渚ф柟鍋滆溅浠跨湡](./ground/mujoco_parallel_parking.md)
* [MuJoCo 鍔ㄦ€侀殰纰嶅眬閮ㄩ伩闅滀豢鐪焆(./ground/mujoco_dynamic_avoidance.md)
* [CARLA 鍋滆溅鍦哄満鏅敓鎴愶紙闄勫甫涓嶄緷璧?CARLA 鐨勫€掕溅鍏ュ簱瑙勫垝鍣級](./ground/carla_parking_lot.md) 鈥斺€?鍦?CARLA 閲岀敾 6 涓溅浣嶏紝鍙︽彁渚涗竴涓函 Python 鐨勫€掕溅鍏ュ簱杞ㄨ抗瑙勫垝鍣紝4 鏉℃柇瑷€鍙洿鎺ヨ窇鍥炲綊
* [MuJoCo 绾㈢豢鐏惎鍋滃皬杞︿豢鐪焆(./ground/mujoco_traffic_light_stop.md)
* [MuJoCo 灏忚溅璺熻溅浠跨湡](./ground/mujoco_car_follow.md)
* [MuJoCo 灏忚溅婊戞枩鍧(./ground/mujoco_slope_car.md)
* [鎮礀杈圭紭绱ф€ュ埗鍔ㄤ豢鐪焆(./ground/cliff_brake.md) 鈥斺€?鐢?MuJoCo 鐗╃悊寮曟搸涓?ROS 涓夎妭鐐归棴鐜疄鐜拌溅澶存祴璺濊Е鍙戠殑婊炲洖绱ф€ュ埗鍔紝闄勫畨鍏ㄥ寘缁滃畾閲忔祴璇曚笌鍧犺惤瀵圭収
* [鑸悜 PID 鍙傛暟鑷暣瀹氫笌鎵嬪伐璇曞噾瀵规瘮](./ground/pid_auto_tuning.md) 鈥斺€?鐢ㄧ户鐢靛櫒鍙嶉娉曡嚜鍔ㄦ眰 Ku/Tu 骞剁瓫閫?PID 鍙傛暟锛屼笌鎵嬪伐璇曞噾鍚屽伐鍐靛姣旇秴璋冧笌璋冭妭鏃堕棿
* [鍩轰簬 Autoencoder 鐨勯浄杈炬暟鎹慨澶嶄笌閬块殰](./ground/lidar_autoencoder_repair.md) 鈥斺€?绂荤嚎璁粌鑷紪鐮佸櫒鍘婚櫎浼犳劅鍣ㄥ櫔澹帮紝淇鍚庢暟鎹€佸叆闃堝€奸伩闅滄帶鍒堕摼璺紝灞曠ず浼犳劅鍣ㄦ暟鎹閿欏眰涓庢帶鍒跺眰瑙ｈ€︾殑璁捐
* [鍦伴潰杞藉叿鐏厜鑷姩鎺у埗](./ground/carla_auto_light.md)
* [闄愰€熸爣蹇楄瘑鍒笌绁炵粡缃戠粶闄愰€熸帶鍒禲(./ground/traffic_sign_speed_control.md) 鈥斺€?MuJoCo 浠跨湡涓溅杞界浉鏈洪噰闆嗛檺閫熸爣蹇楋紝CNN 瀛楃璇嗗埆闄愰€熸暟鍊硷紝闂幆闄愰€熸帶鍒跺樊閫熷皬杞︼紝闄勯€€鍖栫煩闃典笌澶氬満鏅€ц兘璇勪环
* [杞ㄨ抗/閲岀▼璁＄簿搴﹁瘎浼帮紙ATE/RPE锛塢(./ground/trajectory_accuracy_eval.md)
* [RTK 鍙屽樊鏁村懆妯＄硦搴﹀浐瀹氾紙LAMBDA锛塢(./ground/rtk_ambiguity_resolution.md) 鈥斺€?鍙屽樊娴偣瑙?+ LAMBDA 鍘荤浉鍏?+ ratio 妫€楠岋紱20 鍘嗗厓绐楀彛鍩虹嚎璇樊 160.51 mm 鈫?0.89 mm锛岄敊璇浐瀹?0%锛岄檮 2/5/10/20/40 鍘嗗厓鐨勬敹鏁涘鐓?* [鍩轰簬 2D 婵€鍏夐浄杈剧殑钂欑壒鍗℃礇瀹氫綅锛圡CL锛塢(./ground/lidar_mcl_localization.md) 鈥斺€?Gazebo 宸€熻溅 + 360 鏉熸縺鍏夛紝鐢ㄧ函 NumPy 鎵嬪啓绮掑瓙婊ゆ尝锛堣繍鍔ㄦā鍨嬮噰鏍枫€佷技鐒跺満瑙傛祴妯″瀷銆佷綆鏂瑰樊閲嶉噰鏍凤級锛屽苟鐢?MLP 瀛︽帀閲岀▼璁¤繍鍔ㄦ畫宸紱鍥涚粍瀵规瘮涓綅缃宸粠 0.345 m 闄嶅埌 0.020 m

* [鍦伴潰杞藉叿鍔ㄥ姏鎬ф祴璇昡(./ground/carla_vehicle_dynamics_test.md)
* [鍒楄溅 ATO 鑷姩杩愯涓庣珯鍙扮簿纭仠杞(./ground/train_ato_stop.md) 鈥斺€?鎸夌嚎璺檺閫熶笌鍧￠亾鐢熸垚鐩爣閫熷害鏇茬嚎锛岀珯鍙板仠杞﹁宸?0.02锝?.18 m锛堟爣灏?0.3 m锛夛紝鍙︽湁 ATP 瓒呴€熺洃鐫ｄ笌鏅氬埗鍔ㄥ鐓?* [澶氳溅鍗忓悓缂栭槦锛圕ARLA锛塢(./ground/carla_platoon.md) 鈥斺€?Leader 娌垮弬鑰冭建杩归鑸紝3 杈?follower 娌垮悓杞ㄨ抗淇濇寔鎭掑畾寮ч暱闂磋窛璺熻繘鐨勪竴瀛楃旱闃熺紪闃?* [澶氫紶鎰熷櫒铻嶅悎璺熻釜锛圠iDAR+Radar+Camera+IMU锛?D 鍚堟垚浠跨湡涓庣绾块獙璇乚(./ground/carla_sensor_fusion.md) 鈥斺€?澶栧弬鏍囧畾 + 鏃堕棿鍚屾 + EKF 铻嶅悎锛?D 浠跨湡鎻愬崌绾?32%锛岀绾垮洖鏀?30 s 铻嶅悎 578 娆°€丷MSE 0.053 m锛堝潎鍙鐜帮紱CARLA 涓烘湭楠岃瘉鐨勫弬鑰冨疄鐜帮級
* [楂樼簿搴﹀畾浣嶄笌閲嶅畾浣嶏紙AMCL 寮忕矑瀛愭护娉級](./ground/turtlebot3_relocalization.md)

* [涓よ疆鑷钩琛℃満鍣ㄤ汉锛堝€捐PD + 绁炵粡缃戠粶绛栫暐鍏嬮殕锛塢(./ground/balance_bot.md) 鈥斺€?MuJoCo 涓よ疆鍊掔珛鎽嗭紝鍊捐 PD 绔欑ǔ锛?0 s 鏈€澶у€捐 0.96掳锛夛紝琚帹 2 N路s 鍚?3.22 s 鍥炴锛屽苟鐢?MLP 鍏嬮殕鎺у埗寰?* [鍩轰簬閲岀▼璁″弽棣堜笌 A* 绠楁硶鐨勫樊閫熷簳鐩橀潤鎬佸叏灞€璺緞瑙勫垝](./ground/diff_drive_astar_odom_nav.md) 鈥斺€?Gazebo 宸€熷簳鐩樺湪闈欐€佹爡鏍间笂鐢?A* 瑙勫垝鍏ㄥ眬璺緞锛屼粎鍑?`/odom` 閲岀▼璁″仛 30 Hz 绾拷韪棴鐜紝骞剁敤鐪熷€奸噺鍖栬窡韪宸笌閲岀▼璁℃紓绉?* [ROS2 宸€熸満鍣ㄤ汉 A* 鍏ㄥ眬瑙勫垝涓?DWA 灞€閮ㄩ伩闅淽(ground/ros2_dwa_avoidance.md) 鈥斺€?A* 鍏ㄥ眬璺嚎 + DWA 灞€閮ㄨ窡韪紝5 鍦烘櫙 3 鎺у埗鍣ㄥ姣旓紝绐勮蛋寤婁笌 U 褰㈤櫡闃遍€氳繃
* [宸€熸満鍣ㄤ汉閲岀▼璁℃爣瀹氫笌绁炵粡缃戠粶婊戠Щ琛ュ伩锛圧OS 1 + MuJoCo锛塢(./ground/diff_drive_odom_calib.md) 鈥斺€?MuJoCo 鐗╃悊浠跨湡涓嬬殑 catkin 鍖咃紱涓や釜瑙ｈ€﹀疄楠岃鲸璇嗚矾绋?杞窛绯绘暟锛屽啀鐢?MLP 瀛﹁浆鍚戞粦绉荤殑闈炵嚎鎬цˉ鍋匡紝鏂瑰舰璺緞缁堢偣璇樊 2.91 m 鈫?1.94 m 鈫?0.98 m
* [IMU 鍣０ Allan 鏂瑰樊杈ㄨ瘑涓庡€捐婊ゆ尝鏁村畾](./ground/imu_allan_noise_identification.md) 鈥斺€?1 h 闈欐闄€铻鸿褰曡鲸璇?ARW锛堜腑浣嶆暟 +0.46%锛変笌闆跺亸涓嶇ǔ瀹氭€э紙+3.77%锛?5% 鍖洪棿 [鈭?6.7, +44.4]锛夛紝ARW鈫掕搴﹀櫔澹般€丅I鈫掑亸缃父璧帮紱鍊捐鍗″皵鏇?NEES 1.61锛岃繃绋嬪櫔澹板亸灏?4 鍊嶆椂 10.07
* [鏃犲姩鍔涜鍔ㄨ璧帮紙杞緪寮?Rimless Wheel锛塢(./ground/passive_walker.md)
* [鐩告満-婵€鍏夐浄杈惧鍙傛爣瀹歖(./ground/lidar_camera_calibration.md) 鈥斺€?鍚堟垚澶氬Э鎬佹鐩樻牸鍦烘櫙锛孭nP 姹?LiDAR鈫掔浉鏈哄鍙傚苟涓庣湡鍊煎姣旓紝闄勫櫔澹颁笌鎽嗕綅娆℃暟鏁忔劅鎬у疄楠?* [鍓嶈鐩告満杞﹂亾鍋忕棰勮锛堣瑙夋í鍚戝亸绉讳笌鍦板浘鐪熷€煎鐓э級](./ground/carla_visual_lane_departure_warning.md) 鈥斺€?鐢ㄥ墠瑙嗗浘鍍忎及璁℃í鍚戝亸绉伙紝骞朵笌鍦板浘鐪熷€奸€愬抚瀵圭収
* [宸€?AGV 鍧￠亾璧锋杈呭姪锛堥槻婧滆溅锛塢(./ground/hill_start_assist.md) 鈥斺€?MuJoCo 12掳 鏂滃潯锛屽洓杞疆瑙掍繚鎸?PD + 鍧″害鍓嶉锛屾澗鍒硅溅 3 s 鍚庢簻 2.18 m 闄嶅埌 0.008 m
* [鍦伴潰绉诲姩搴曠洏閫熷害鎸囦护瀹夊叏鐩戠潱](./ground/cmd_vel_guard.md) 鈥斺€?瀵?`/cmd_vel` 鍋氶檺骞呫€佹€ュ仠銆佽秴鏃朵笌闈炴硶鍊兼嫤鎴紝鏃犻渶浠跨湡鐜
* [巡线小车仿真（色带中线 PD 跟踪）](./ground/line_follower_car.md) —— 一排虚拟光电传感器读取线偏差，pure pursuit 预瞄 + PD 转向闭环引导沿黑线巡线
* [VRU 鍐茬獊椋庨櫓鍥綸(./ground/vru_conflict_risk_map.md) 鈥斺€?鎸夋椂闂村榻愯嚜杞︿笌琛屼汉銆佸効绔ュ拰楠戣鑰呰建杩癸紝杈撳嚭鏈€灏忚窛绂汇€乀TC 鍜岄闄╃瓑绾?* [閲岀▼璁″仴搴风洃瑙嗭紙鎵撴粦 / 鍫佃浆 / 鍙嶅悜妫€娴嬶級](./ground/odom_health_monitor.md) 鈥斺€?姣旇緝 `/cmd_vel` 涓?`/odom` 鐨勯€熷害姣斿€硷紝璇嗗埆鎵撴粦銆佸牭杞笌鍙嶅悜杩愬姩

## 5. 绌哄煙杞藉叿 <span id='air_vehicle'></span>

* [澶氭棤浜烘満绌哄煙鐩戞祴锛堝杈瑰舰绂侀鍖轰笌鏈洪棿鍐茬獊锛塢(./air/multi_uav_airspace_monitor.md) 鈥斺€?闈㈠悜澶氭満杞ㄨ抗鐨勭數瀛愬洿鏍忋€佹渶杩戞帴杩戣窛绂诲拰鍐茬獊瑙ｈ劚寤鸿

* [澶氭棆缈煎崟妗ㄥけ鏁堝悗鐨勬偓鍋滃彲琛屽煙](./air/uav_rotor_failure_env.md) 鈥斺€?闆跺Э鎬佸姏鐭╃害鏉熶笅鐨勬渶澶ф€绘帹鍔涳紝瀵规瘮鍥?鍏?鍏棆缈兼槸鍚﹀繀椤昏嚜鏃嬶紝12 椤规祴璇?
* [鏃犱汉鏈哄姩鎬佺數瀛愬洿鏍忛娴嬮璀(./air/uav_dynamic_geofence_guard.md) 鈥斺€?閽堝绉诲姩涓存椂绂侀鍖鸿绠楅娴嬪噣绌恒€佹渶杩戞帴杩戞椂闂村拰瑙勯伩鏂瑰悜锛屽苟闄?ROS 2 Humble 瀹炶窇璇佹嵁

* [winter 鍦烘櫙鏃犱汉鏈哄渾鍛ㄩ琛宂(./air/winter_circle.md)
* [AirSim ROS 1 Noetic PPO 鑱旇皟](./air/airsim_rl_planner_ros1.md)
* [鏃犱汉鏈哄埗鍔ㄦ棫鍏ュ彛](./ground/mujoco_drone_distance_stop.md)

* [Town10 绔嬮潰鑷富宸¤埅涓庡浘鍍忛噰闆哴(./air/town10_facade_cruise_capture/index.md)

* [Town10 骞曞鍥惧儚鐥呭璇嗗埆](./air/town10_facade_defect_detection/index.md)

* [AirSim Unity 鏃犱汉鏈烘洸绾跨粫鏌遍伩闅滃疄楠宂(./air/airsim_obstacle_avoidance.md)
* [AirSim Unity 鏃犱汉鏈洪珮搴﹁嚜閫傚簲瓒婇殰瀹為獙](./air/airsim_height_aware_overfly.md) 鈥斺€?娣卞害鍥鹃€愬垪鎭㈠闅滅椤惰竟锛岀煯澧欏師鍦扮埇鍗囪秺杩囥€侀珮闅滅閫€鍥炴按骞崇粫琛岋紱57 椤圭绾挎祴璇?+ 2026-11-09 涓ゆ瓒婇殰瀹為锛堣秺闅滃悗淇濇寔 5.2 m銆佸埌鐐硅宸?<0.7 m锛涚浉鏈哄亸绉讳慨姝ｅ悗 committed 绾?2.6 m锛屽皻鏈椋烇級
* [鏃犱汉鏈烘繁搴︾浉鏈虹缁忕綉缁滈伩闅滈琛岋紙MuJoCo锛塢(./air/uav_mujoco_depth_avoidance.md) 鈥斺€?64脳64 鏈鸿浇娣卞害鍥?鈫?numpy CNN 鈫?涓夋墖鍖洪€氳搴?鈫?閫熷害/鍋忚埅闂幆锛? 鍦烘櫙 脳 5 瀹炰緥鍏?15/15 鎴愬姛
* [鏃犱汉鏈虹潃闄嗛樁娈佃瘑鍒笌鎺ュ湴杞借嵎棰勬祴](./air/landing_assessment.md)
* [楂樺害涓庡€捐妫€娴嬭瘎浼癩(./air/air_ground_detection_benchmark.md) 鈥斺€?缁熻涓嶅悓鐩告満楂樺害鍜屼刊浠拌涓嬬殑妫€娴嬬簿搴︺€佸彫鍥炵巼涓庡皬鐩爣鍙洖鐜?
* [Fixed-wing SITL preflight](./air/fixed_wing_sitl_preflight.md): static configuration checks for PX4/ArduPilot fixed-wing SITL
* [鏃犱汉鏈烘祴璺濆埗鍔ㄤ笌绁炵粡鎺у埗](./air/mujoco_uav_range_neural_braking.md)
* [鏃犱汉鏈烘祴璺濆埗鍔ㄨ建杩规寚鏍囧垎鏋怾(./air/mujoco_uav_braking_metrics.md)
* [鏃犱汉鏈烘祴璺濆嚑浣曚竴鑷存€ф鏌(./air/mujoco_uav_range_sensor_quality.md)

* [鏃犱汉鏈鸿浇鑽疯川閲忎及璁(./air/payload_mass_estimation.md)
* [鏃犱汉鏈鸿浇鑽烽噸蹇冨亸绉讳笌閰嶅钩鐩戞祴](./air/uav_payload_balance_guard.md) 鈥斺€?鍒╃敤宸﹀彸鎺ㄥ姏宸€佹粴杞慨姝ｅ拰妯憜鍝嶅簲浼拌妯悜閲嶅績鍋忕Щ锛岃緭鍑洪厤骞冲拰瀹夊叏鍖呯嚎鍛婅
* [AirLib 浼犳劅鍣ㄦ秷鎭洖褰抅(./air/airlib_message_regression.md) 鈥斺€?鍦?ROS 妗ユ帴鍓嶆牎楠?IMU銆丟PS銆丩iDAR 鍜岄噷绋嬭鏁版嵁濂戠害
* [鏃犱汉鏈?GPS 娆洪獥涓庡畾浣嶅畬鏁存€х洃娴媇(./air/uav_gps_integrity_guard.md) 鈥斺€?铻嶅悎浣嶇疆璺冲彉銆侀€熷害涓€鑷存€у拰 IMU 宸紓锛岃緭鍑?GPS 鍙俊銆佷氦鍙夋鏌ユ垨鎷掔粷寤鸿

* [UAV mission energy budget](./air/uav_energy_budget.md) ? estimates energy, reserve and endurance for hover, climb and cruise segments

* [鏃犱汉鏈虹數鑺仴搴蜂笌涓嶅钩琛￠璀(./air/uav_battery_health_guard.md) 鈥斺€?鏍规嵁鍗曚綋鐢靛帇宸€佹俯搴︺€佸唴闃诲拰璐熻浇鍘嬮檷璇嗗埆寮辩數鑺紝杈撳嚭闄愯浇鎴栧氨杩戦檷钀藉缓璁?

* [鏃犱汉鏈轰换鍔＄鐞嗕笌瀹夊叏鐘舵€佹満](./air/uav_mission_safety_manager/overview.md)

* [鏃犱汉鏈洪琛岃建杩圭被鍨嬭瘑鍒笌 ROS2 鑷姩浠诲姟鏃ュ織](./air/flight_pattern_recognition.md)

* [娣卞害鍥剧鍒扮绌胯秺闂ㄧ珵閫焆(./air/uav_depth_gate_racing_e2e.md)

* [鏃犱汉鏈洪仴娴嬪紓甯告娴嬩笌 ROS2 鍦ㄧ嚎璇婃柇](./air/telemetry_diagnostics.md)

* [浣庣┖澶氭簮姘旇薄鎵板姩涓嬫棤浜烘満褰卞搷棰勬祴涓庨闄╁垎绾(./air/uav_weather_risk.md)

* [鏃犱汉鏈虹伀鐏炬帰娴嬩笌鑷富宸℃](./air/fire_detection_drone.md) 鈥斺€?HSV/ONNX 鐏劙妫€娴嬮厤鍚堟湁闄愮姸鎬佹満锛屾敮鎸佸紦瀛楀舰銆佽竟鐣屼笌铻烘棆涓夌宸℃鍦烘櫙锛屽彂鐜扮伀鐏惧悗鑷姩鎮仠纭銆佺洏鏃嬪彇璇佸苟杩旇埅
* [閰嶇疆 AirSim 瀹㈡埛绔幆澧冨苟杩炴帴妯℃嫙鍣紙Windows 鏈満 / WSL2锛塢(./air/airsim_client_setup.md)

* [寤虹珛铏氭嫙鏈哄拰绌哄煙杞藉叿涔嬮棿鐨勮繛鎺(./air/setup_and_connect.md)
* [鏃犱汉鏈虹洰鏍囬珮搴﹂檺骞呫€佸彉鍖栫巼绾︽潫涓庤秴鏃朵繚鎸乚(./air/uav_altitude_command_guard.md)
* [鏃犱汉鏈哄亸鑸寚浠ゆ渶鐭矾寰勪笌瑙掗€熷害闄愬箙](./air/uav_yaw_command_guard.md) 鈥斺€?灏嗗亸鑸宸槧灏勫埌 `[-pi, pi)`锛岄伩鍏嶈法 180掳 鏃剁粫杩滆矾锛屽苟闄愬埗 `Twist.angular.z`
* [鏃犱汉鏈洪浄杈綝QN寤哄浘涓庣鍒扮鎺у埗](./air/uav_lidar_dqn_navigation/index.md) 鈥斺€?24 鎵囧尯闆疯揪鐗瑰緛 + Dueling Double DQN 鑷富瀛︿範閬块殰瀵艰埅锛実mapping 鍚屾寤哄浘锛屽浘鍍忕鍒扮 DQN 鎺у埗

* [鏃犱汉鏈烘縺鍏夐浄杈句笁缁村畨鍏ㄨ蛋寤婁笌鑷€傚簲楂樺害閬块殰](./air/uav_lidar_safety_corridor.md) 鈥斺€?鍩轰簬 OpenHUTB 婵€鍏夐浄杈剧偣浜戦€夋嫨瀹夊叏楂樺害锛屽苟瀹屾垚涓栫晫绯婚€熷害闂幆椋炶

* [鏃犱汉鏈烘渶灏忓姞鍔犻€熷害杞ㄨ抗鐢熸垚涓庤窡韪猐(./air/uav_minimum_jerk_tracking.md) 鈥斺€?鐢熸垚鍒嗘浜旀杞ㄨ抗锛堟鍐?jerk 杩炵画锛夛紝骞朵笌绾挎€у弬鑰冨姣旇窡韪宸拰鍔犲姞閫熷害宄板€?* [鏃犱汉鏈虹┖閫?鍦伴€熶笁瑙掍及椋庝笌鍙娴嬫€(./air/uav_wind_estimation.md) 鈥斺€?椋庝笁瑙掓畫宸渶灏忎簩涔?+ 淇℃伅鐭╅樀鍙娴嬫€э紱鎮仠/鐩寸嚎涓嶅彲浼帮紙鏉′欢鏁?2914-3600锛夛紝鍦嗗懆鏈哄姩椋庨€?RMSE 0.042 m/s锛堢湡鍊?3.6 m/s锛?
* [鏃犱汉鏈虹浉鏈轰簯鍙颁袱杞寸ǔ瀹氭帶鍒禲(./air/uav_gimbal_stabilization.md) 鈥斺€?浜岀淮鐩爣瑙嗙嚎 PID 璺熻釜銆佽閫熷害闄愬箙鍜屾鍖烘帶鍒讹紝闄勪豢鐪熸寚鏍囦笌 CSV
* [鏃嬬考妗ㄥ皷椹但鏁颁笌妗ㄧ洏杞借嵎](./air/uav_prop_tip_mach.md) 鈥斺€?鐢辨〃寰勩€佽浆閫熶笌娓╁害绠楁〃灏栭€熷害涓庨┈璧暟锛堥粯璁?10 瀵告〃 9000 rpm 鏃?0.35锛屽畨鍏級锛岀敱鏁存満璐ㄩ噺涓庢〃鐩橀潰绉畻妗ㄧ洏杞借嵎涓庢偓鍋滆瀵奸€熷害锛?6.8 N/m虏銆?.28 m/s锛?
* [鏃犱汉鏈?IMU 涓庢皵鍘嬮珮搴﹁瀺鍚圿(./air/uav_altitude_sensor_fusion.md) 鈥斺€?瀵规瘮姘斿帇楂樺害銆佸姞閫熷害绉垎鍜屼竴缁村崱灏旀浖铻嶅悎锛岄檮楂樺害鍝嶅簲鍥句笌璇樊鎸囨爣

* [绌哄煙杞藉叿鐨勫叓鍙夋爲涓夌淮瀵昏矾](./air/octree_uav_3d_pathfinding/env_setup.md)

* [鐐逛簯杞叓鍙夋爲鍗犵敤鍦板浘](./air/octree_uav_3d_pathfinding/occupancy_mapping.md)

* [鍏弶鏍戜笂鐨?A* 鍏ㄥ眬瀵昏矾](./air/octree_uav_3d_pathfinding/astar_planning.md)

* [绌哄煙妯℃嫙鍣ㄧ殑 ROS 灏佽鍣╙(./air/ros_pkgs.md)
* [鏃犱汉鏈轰笌 ROS 鐨勬ˉ鎺ユā鍧梋(./air/carlair_ros_bridge.md)
* [鏃犱汉鏈?LiDAR 鍦伴潰/闅滅鍒嗗壊](./air/uav_lidar_ground_filter.md)
* [鏃犱汉鏈哄眿椤堕檷钀絔(./air/rooftop_landing.md) 鈥斺€?鐢ㄦ満杞?LiDAR 妫€娴嬪眿椤跺钩闈紝鍙栬疆寤撶殑鏈€澶у唴鍒囧渾鍦嗗績浣滀负闄嶈惤鐐癸紝鑷富椋炴姷鍏朵笂鏂瑰悗鍨傜洿闄嶈惤
* [鏃犱汉鏈哄眿椤堕檷钀斤紙瀛︿範鍨嬭惤鐐归€夋嫨锛塢(./air/rooftop_landing_nn.md) 鈥斺€?鐢ㄧ偣浜戦珮搴﹀浘 + 灏?CNN 鐩存帴鍥炲綊灞嬮《钀界偣锛涘嚬褰㈠眿椤讹紙U/L/澶╀簳锛変笌绋€鐤忕偣浜戜笅姣斿嚫鍖呮渶澶у唴鍒囧渾鏇寸ǔ锛岄檮涓夌粍娑堣瀺瀵规瘮
* [鏃犱汉鏈洪檷钀借繃绋嬬洃鎺э紙鎸囦护-杩愬姩涓€鑷存€э級](./air/uav_landing_monitor.md) 鈥斺€?鍦ㄧ嚎鏍￠獙銆岄€熷害鎸囦护 vs 瀹為檯楂樺害鍙樺寲銆嶏紝鎶撯€滃枈浜嗕笉鍔?/ 鎺夊緱娌′汉绠?/ 瓒呮椂娌¤惤鍦扳€濊繖绫婚潤榛樻晠闅滐紝杈撳嚭鍛婅銆佺姸鎬?JSON 涓?CSV 鎶ュ憡
* [绉诲姩骞冲彴锛堣溅/鑸癸級绮惧噯闄嶈惤](./air/uav_moving_platform_landing.md) 鈥斺€?鍙悆涓€璺甫寤惰繜鐨勫钩鍙颁綅缃紝鍦ㄧ嚎浼伴€熷害銆侀娴嬬浉閬囩偣锛岃惤鐐硅宸?0.03 m锛堣拷瀹炴祴浣嶇疆鐨勬湸绱犲仛娉?0.48 m 涓旇惤涓嶅噯锛夛紝闄勫洓绉嶅埗瀵肩瓥鐣ョ殑瀹氶噺瀵圭収
* [鏃犱汉鏈洪敭鐩樻帶鍒禲(./air/uav_keyboard_control.md)

* [鍩轰簬 PPO 鐨勬棤浜烘満瀵艰埅閬块殰](./air/uav_ppo_nav.md)
* [鏃犱汉鏈哄畾楂樻棩蹇楄宸笌鎶楁壈鎭㈠鏃堕棿璇勪及](./air/uav_hover_log_eval.md)

* [鍩轰簬娣卞害寮哄寲瀛︿範鐨勬棤浜烘満鏈€浼樿矾寰勬煡鎵撅紙PPO/SAC锛塢(./air/drl_drone_path_planning.md) 鈥斺€?鎶?DRL-drones 鐨?PyBullet 鐜閲嶆瀯涓?ROS 鍖咃細28 缁磋娴?+ 4 缁存満浣撶郴閫熷害鎸囦护锛岃缁冪敤 Stable-Baselines3銆侀儴缃茬敤绾?NumPy锛屽苟涓庡嚑浣曞熀绾垮悓鍦哄姣?
* [鍩轰簬 PPO 鐨勬棤浜烘満鍥哄畾璺嚎宸¤埅](./air/uav_route_cruise.md) 鈥斺€?娌跨粰瀹氶棴鍚堣埅绾垮贰鑸紝閬囧帇鍦ㄨ埅绾夸笂鐨勯殰纰嶆椂涓存椂鍋忕缁曡

* [鏃犱汉鏈哄鑸己鍖栧涔犲姣斿疄楠岋紙PPO/SAC/TD3锛塢(./air/uav_rl_benchmark.md)

* [绁炵粡娈嬪樊鍔ㄥ姏瀛︿笌瀛︿範寮忚建杩硅窡韪猐(./air/uav_neural_residual_control.md)
* [鍩轰簬 DQN 鐨勬棤浜烘満瀵艰埅閬块殰](./air/uav_dqn_nav.md) 鈥斺€?涓?PPO 鍚岀幆澧冨悓瑙傛祴锛屼粎鏇挎崲涓?DQN 绂绘暎鍔ㄤ綔绠楁硶锛岀敤浜庣鍒扮妯″瀷/绠楁硶瀵规瘮
* [鍩庡競鍔ㄦ€佷氦閫氫笅鐨勬棤浜烘満閬块殰锛圥PO + DAgger锛塢(./air/uav_traffic_nav.md) 鈥斺€?鐢?CARLA 杞︽祦鍋氬姩鎬侀殰纰嶏紱瑙勫垯涓撳绀鸿寖 + 琛屼负鍏嬮殕 + DAgger锛岃法璺垚鍔熺巼 48%卤3.6%锛岄珮浜庤椽蹇冿紙39%锛変笌閫熷害闅滅娉曪紙19%锛?* [鏃犱汉鏈簆po妯″潡鐮旂┒](./air/uav_experiments.md) 鈥斺€?鎶婇敭鐩樻帶鍒躲€丳PO 瀵艰埅銆佺畻娉曞姣斻€佽埅绾垮贰鑸€佸姩鎬佷氦閫氫簲涓疄楠屽悎骞跺埌涓€椤碉紱鍚勫疄楠岀嫭绔嬮〉闈粛鐒朵繚鐣?
* [鏃犱汉鏈虹粓绔敭鐩橀仴鎺у櫒](./air/drone_teleop.md)

* [AirSim鏃犱汉鏈洪敭鐩橀仴鎺т笌鏈鸿浇浜戝彴鎺у埗妯″潡](./airsim_drone_gimbal_teleop/README.md)

* [鏃犱汉鏈烘満杞戒簯鍙扮洰鏍囦涪澶遍噸鎹曡幏涓庤杞磋宸瘎浼癩(./air/uav_gimbal_reacquisition.md)

* [鏃犱汉鏈鸿瑙夋劅鐭ョ疆淇″害閫€鍖栦繚鎶(./air/uav_perception_confidence_guard.md) 鈥斺€?缁煎悎妫€娴嬬疆淇″害銆侀娴嬬喌銆佹帹鐞嗗欢杩熷拰甯ч檲鏃у害锛岃瘑鍒劅鐭ラ€€鍖栧苟杈撳嚭淇濇寔鎴栬繑鑸缓璁?
* [鏃犱汉鏈哄簲鎬ョ潃闄嗙偣瀹夊叏璇勪及](./air/uav_emergency_landing_selector.md) 鈥斺€?浠庡潯搴︺€佺矖绯欏害銆侀殰纰嶃€佷汉鍛橀闄╁拰鑳介噺瑁曢噺涓瓫閫夊畨鍏ㄨ惤鐐癸紝闄?ROS 2 Humble 瀹為檯 launch 楠岃瘉

* [鍩轰簬 ROS 娑堟伅瑙ｈ€︾殑鏃犱汉鏈洪敭鐩橀仴鎺(./air/drone_ros_teleop.md)

* [棰勮鑸嚎椋炶妯℃嫙鍣╙(./air/flight_path_simulator.md) 鈥斺€?绾?Python 绂荤嚎鑴氭湰锛屾寜棰勮鏃堕棿琛ㄦ挱鏀句竴娈靛贰鑸琛屽苟鐢熸垚鏁版嵁闆嗕笌鍙鍖栵紝涓嶄緷璧?ROS/浠跨湡鍣?
* [鏃犱汉鏈鸿埅鐐硅建杩硅窡韪紙PID 鎺у埗锛塢(./air/waypoint_tracking.md)

* [鍩轰簬涓茬骇PID鐨勫洓鏃嬬考鑸偣瀹氱偣鎮仠涓庢姉椋庢壈浠跨湡](./air/quad_cascade_pid_hover_wind.md) 鈥斺€?绾?Python 6 鑷敱搴﹀洓鏃嬬考鍒氫綋鍔ㄥ姏瀛︿豢鐪燂紝浣嶇疆-濮挎€?瑙掗€熺巼涓茬骇 PID 闂幆锛屽惈鎭掑畾椋?闃甸/婀嶆祦鎵板姩锛岄獙璇佽埅鐐硅窡韪笌瀹氱偣鎮仠鐨勬姉椋庢壈鑳藉姏

* [鍩轰簬 GRU 鐨勬棤浜烘満椋炶鐘舵€侀娴嬩笌 ROS2 鍦ㄧ嚎璇樊鍒嗘瀽](./air/state_prediction.md)

* [MuJoCo 鍩庡競灞嬮《鍏変紡瑕嗙洊鐜囨祴閲廬(./air/mujoco_uav_rooftop_pv_coverage_survey.md) 鈥斺€?閫氳繃杞婚噺灞嬮《鍦烘櫙銆佸線澶嶆潯甯﹁埅绾垮強鍚屾 RGB-鍏変紡鎺╃爜鏋勫缓鍙鐜扮殑娴嬮噺鏁版嵁鍩虹

* [MuJoCo 灞嬮《鍏変紡瑕嗙洊鐜囨祴閲忕浜屽ぉ](./air/mujoco_uav_rooftop_pv_coverage_survey_day2.md) 鈥斺€?杞婚噺璇箟鍒嗗壊銆佽埅杩规帶鍒躲€丷OS 2 鎺ュ彛涓庝笁绉嶅竷灞€璇勪环
* [鏃犱汉鏈洪€氫俊閾捐矾閫€鍖栦繚鎶や笌鏂仈椋庨櫓棰勬祴](./air/uav_link_outage_guard.md) 鈥斺€?铻嶅悎 RSSI銆佸欢杩熴€佷涪鍖呬笌閬ユ祴闄堟棫搴︼紝棰勬祴閾捐矾椋庨櫓骞惰緭鍑洪檷閫熴€佷繚鎸佹垨杩旇埅寤鸿

* [绁炵粡瑙嗚鎯€ч噷绋嬭涓庝笁鍚庣 SLAM 瀵规瘮](./air/uav_neural_vio_slam.md)

* [MuJoCo 鍥涙棆缈间豢鐪熶笌 ROS2 妗ユ帴搴曞骇](./air/uav_mujoco_sim.md)
* [MuJoCo 鍥涙棆缈煎瀭鐩撮€氶亾 PPO 瀹氶珮涓庢姉鎵版帶鍒禲(./air/uav_vertical_ppo.md)

* [鏃犱汉鏈烘墽琛屽櫒鏁呴殰娉ㄥ叆涓庢帶鍒堕€€鍖栬娴媇(./air/uav_actuator_fault_sim.md) 鈥斺€?鍦?MuJoCo 搴曞骇涓婃彃鍏ュ彲缂栫▼鐨勬〃鏁呴殰锛堝畬鍏ㄥけ鏁?/ 鎺ㄥ姏琛板噺 / 鍗℃ / 娓愯繘閫€鍖栵級涓?IMU 鏁呴殰锛屽疄娴?鍗曟〃瀹屽叏澶辨晥 0.64 s 蹇呭潬銆佹妸鎹熷け鎺ㄥ姏鍧囨憡缁欏叾浣欎笁妗ㄤ篃鏁戜笉鍥炴潵"锛屼负鍚庣画绁炵粡瀹归敊椋炶妯″潡鎻愪緵鏁版嵁涓庤瘎娴嬪彴
* [鍥涙棆缈煎悐鎸傝礋杞介槻鎽嗘帶鍒禲(./air/uav_slung_load.md) 鈥斺€?MuJoCo 鍙版灦涓婂姣?PD銆乑V 杈撳叆鏁村舰涓庢憜瑙掑弽棣堬紝娈嬩綑鎽嗚浠?7.0掳 闄嶅埌 0.1掳

* [鏃犱汉鏈烘〃鏁呴殰鍋ュ悍搴︿及璁(./air/uav_rotor_fault_detector_nn.md) 鈥斺€?鐢ㄦ満杞?IMU 涓庢帶鍒跺櫒鎸囦护锛?3 缁寸壒寰侊級缁?1D-CNN+GRU 瀹炴椂鍥炲綊鍥涙〃鍓╀綑鎺ㄥ姏鏉冮檺锛屽崟妗ㄥ畬鍏ㄥけ鏁?0.10 s 妫€鍑恒€佽鎶ョ巼 0锛屽悓鏃舵彁渚?ROS2 鑺傜偣涓庡湪绾夸及璁℃帴鍙?
* [鏃犱汉鏈虹紪闃熼琛宂(./air/uav_formation_flight.md) 鈥斺€?闀挎満鎸夎埅鐐瑰贰鑸€佸儦鏈轰繚鎸侀槦褰紙涓€瀛?绾甸槦/涓夎鍙姩鎬佸垏鎹級锛屼笁鏋跺叡鐢ㄤ竴鏉?AirSim RPC锛屼緷娆¤捣椋炪€佷綆绌哄睍寮€鍚庤繘鍏ヤ换鍔?* [绁炵粡瀹夊叏杩囨护鍣╙(./air/uav_neural_safety_filter.md)
* [鏃犱汉鏈烘帶鍒舵潈闄愰ケ鍜屼笌绉垎楗卞拰鐩戞祴](./air/uav_control_authority_guard.md) 鈥斺€?瀵规瘮鏈熸湜涓庡疄闄呰閫熷害銆佹墽琛屽櫒楗卞拰鍜岀數鍘嬩笅闄嶏紝璇嗗埆鎺у埗鏉冮檺涓嶈冻骞惰緭鍑烘満鍔ㄩ檺鍒跺缓璁?
* [浣庣┖杞藉叿鐨?ROS 绀轰緥鏁欑▼](https://openhutb.github.io/air_doc/airsim_tutorial_pkgs/)
* [鎵嬪娍鎺у埗鏃犱汉鏈篯(./air/gesture_control_drone.md)

* [AP-CPP 涓诲姩鎰熺煡瑕嗙洊璺緞瑙勫垝](./ap_cpp_overfomo.md) 鈥斺€?鍩轰簬 AirSim 鐨勬棤浜烘満涓诲姩鎰熺煡瑕嗙洊璺緞瑙勫垝锛屽湪 OverFOMO 鑷€傚簲瑕嗙洊瑙勫垝鐨勫熀纭€涓婅繘涓€姝ュ喅瀹氥€岃鍘诲摢閲岀湅銆?
* [鏃犱汉鏈鸿埅娴嬩换鍔¤鍒掞紙GSD/閲嶅彔搴?WPML锛塢(./air/survey_mission_planner.md) 鈥斺€?鐢辩浉鏈哄弬鏁板拰鐩爣 GSD 鍙嶇畻鑸珮銆佽埅甯﹂棿璺濄€佹媿鐓ч棿璺濅笌鑸偣锛屽鍑?CSV/KML/WPML

* [鏃犱汉鏈鸿埅鐐逛换鍔￠琛屽墠鏍￠獙](./air/uav_waypoint_preflight_validator.md) 鈥斺€?妫€鏌?ENU 鐩稿鑸偣鐨勯珮搴︺€侀噸澶嶇偣銆佺埇鍗囪銆佽浆寮銆佽埅绋嬪拰淇濆畧 ETA锛屽苟杈撳嚭 JSON 涓?RViz 棰勮

* [YOLO 鎰熺煡涓庢棤浜烘満鎺у埗](./air/openhutb_yolo_mlp_control/README.md)

* [璇箟鍒嗗壊寤哄浘涓庤涔夎矾寰勮鍒抅(./air/uav_semantic_mapping_nav.md)

* [AllocNet 鍥涙棆缈奸伩闅滆鍒掍笌閿洏閬ユ搷浣淽(./air/allocnet_teleop.md) 鈥斺€?鍦ㄥ涔犲瀷鏃堕棿鍒嗛厤鐨勯伩闅滆建杩硅鍒掑熀纭€涓婏紝琛ラ綈閿洏鑸偣涓嬪彂銆佸湴鍥惧父椹昏浆鍙戜笌杞ㄨ抗璁板綍鐨勪汉鏈轰氦浜掑眰
* [鏃犱汉鏈烘満杞界浉鏈鸿瑙夌洰鏍囪窡韪猐(./air/uav_camera_tracking.md) 鈥斺€?绁炵粡缃戠粶鎰熺煡锛堝浘鍍忊啋鐩爣鍍忕礌鐑浘锛変笌鎺у埗缃戠粶瑙ｈ€﹁缁冿紝涓庣鍒扮绛栫暐鍦ㄩ潤姝?鍦嗗懆/閬尅/闃甸鍥涗釜鍦烘櫙涓嬮棴鐜姣?
* [鐘舵€佽瘑鍒笌杞ㄨ抗缁樺埗](./air/drone_trajectory_logger.md)

* [鍩轰簬 ROS 2 鐨勭椋炲尯锛堢數瀛愬洿鏍忥級鍔ㄦ€佹娴嬩笌瀹夊叏棰勮绯荤粺](./air/geofence.md)

* [鍗曢棬娣卞害瑙嗚浼烘湇锛堥棬涓績鍥炲綊锛塢(./air/uav_gate_center_servo.md) 鈥斺€?12脳16 娣卞害鍥惧洖褰掗棬涓績锛屾瘮渚嬫帶鍒跺櫒杈撳嚭 m/s 閫熷害
* [鏃犱汉鏈烘繁搴︾浉鏈鸿建杩硅窡韪紙CNN 琛屼负鍏嬮殕锛塢(./air/uav_depth_track_nn.md) 鈥斺€?娣卞害鐩告満鎰熺煡 + 缁欏畾鍦嗚建杩硅窡韪紝CNN 杈撳嚭閫熷害鎸囦护

* [RflySim 鍗曟満璧烽涓庣鍙ｆ晠闅滄帓鏌ワ紙琛ュ厖瀹為獙锛塢(./air/rflysim_sitl_first_flight.md)


* [绂侀鍖烘娴嬫ā鍧梋(no_fly_zone_check/index.md)

* [MuJoCo鏃犱汉鏈哄箷澧欏畾璺濇壂鎻廬(air/mujoco_facade_capture/index.md)

* [AirSim 鏃犱汉鏈烘姉椋庢壈琛ュ伩锛圡LP锛塢(./air/uav_airsim_wind_rejection.md) 鈥斺€?IMU 鏃跺簭鍔犱綅缃宸繘 MLP锛岀洿鎺ヨ緭鍑?xy 琛ュ伩閫熷害锛涗晶椋庝笅骞冲潎鍋忕Щ浠?14.68 m 闄嶅埌 3.42 m锛?77%锛夛紝楠岃瘉 R虏 0.997

* [AirSim 鏃犱汉鏈烘繁搴﹂伩闅滐紙CNN 绔埌绔帶鍒讹級](./air/uav_airsim_depth_obstacle_avoidance.md) 鈥斺€?鍓嶈娣卞害 64脳64 杩涙墜鍐?CNN锛屽嚭鍋忚埅瑙掗€熺巼涓庣洰鏍囬珮搴︼紝楠岃瘉闆?MSE 0.0640 / R虏 0.298

## 6. 姘村煙杞藉叿  <span id='water_vehicle'></span>

### 鎰熺煡

* [姘翠笅澹板憪 SLAM 鍗犳嵁鏍呮牸寤哄浘涓庤嚜涓婚伩闅滃鑸猐(./water/rov_sonar_slam_navigation.md)

* [姘翠笅 ROV AprilTag 瑙嗚瀹氫綅涓庡畾鐐瑰贰鑸豢鐪焆(./water/rov_apriltag_cruise.md)

* [姘翠笅 ROV 瑙嗚寮曞鐨勬矇鑸圭粨鏋勫贰妫€閲囨牱浠跨湡](./water/rov_wreck_inspection.md)

* [姘翠笅 ROV 娴峰簳绠￠亾寰€杩斿贰妫€锛堣瑙夋劅鐭?+ EKF-SLAM + 绔埌绔級](./water/rov_pipeline_follow.md) 鈥斺€?140掳 骞胯鍓嶈鐩告満 + 閫愬垪娣卞害锛岃壊搴︾紪鐮佸簲绛斿櫒鍋?EKF-SLAM锛岀骇鑱旀帶鍒舵部绠￠亾鍋忕疆 0.9 m 瀹屾垚 A鈫払鈫扐 寰€杩旓紱鍥涘満鏅紙鐩寸/寮/妯祦/娴戞按锛壝?浜旂瓥鐣ュ姣旓紝鍚?CNN 鎰熺煡涓庣鍒扮绛栫暐娑堣瀺

* [鏂板姘翠笅涓夌淮鍦板舰娴嬬粯妯″潡](./water/underwater_sonar_mapping.md)

* [渚ф壂澹板憪鍥惧儚浠跨湡涓?CNN 娴峰簳鐩爣鍒嗙被](./water/mjc_rov_sonar_cnn.md)
* [姘翠笅 AUV 鐭╁舰宸¤埅涓庤瑙夊弻鍚戦伩闅滀豢鐪焆(./water/auv_end2end.md) 鈥斺€?ROS2 + Gazebo Classic锛屽洓鐘舵€佺煩褰㈠贰鑸笌鍗曠洰鏆楀尯妫€娴嬪弻鍚戦伩闅?
* [娴戞祳姘翠綋瑙嗚澧炲己涓庣洰鏍囪拷韪紙ROS 2锛屽悎鎴愯棰戞紨绀猴級](./water/water_vision_enhancement.md) 鈥斺€?閫氶亾澧炵泭鏍℃銆佺櫧骞宠　銆丆LAHE 涓庢殫閫氶亾鍘绘暎灏勫寮猴紝KCF/CSRT/MOSSE 鐩爣杩借釜锛岄檮鍚堟垚娴戞祳姘翠綋婕旂ず鑺傜偣

* [姘撮潰鏃犱汉鑹囷細婵€鍏夐浄杈惧缓鍥句笌绁炵粡缃戠粶灞€閮ㄨ鍒抅(./water/usv_mujoco_nn.md) 鈥斺€?MuJoCo 涓夎嚜鐢卞害鑸逛綋锛屽皠绾挎縺鍏夐浄杈?+ log-odds 鍗犳嵁鏍呮牸寤哄浘锛孧LP 杈撳嚭灞€閮ㄧ洰鏍囩偣瀹炵幇鑷富閬块殰锛屽皝瑁呬负 ROS Noetic 鑺傜偣

### 瑙勫垝

* [姘翠笅澶氫紶鎰熷櫒鎰熺煡涓?3D 杞ㄨ抗璺熻釜鎺у埗](./water/rov_trajectory_tracking.md)

* [姘翠笅 ROV 瀵规帴浠诲姟锛氬０鍛愭壂鎻?+ CNN 鏍囪妫€娴?+ 閫艰繎瀵艰埅](./water/mjc_rov_docking_nav.md)

* [鍩轰簬鐑姏鍥剧殑娲嬫祦骞叉壈涓?ROV 鑷€傚簲璺緞瑙勫垝](./water/water_rov_path_planning.md)

### 鎺у埗

* [姘村煙杞藉叿绀轰緥锛堟墜鏌?/ 鑸偣 / 娣卞害鑸悜鎸囦护锛塢(./water/holoocean_examples.md) 鈥斺€?澶氫唬鐞嗘墜鏌勬帶鍒躲€佺浉鏈?HUD 涓庨厤缃枃浠剁粨鏋?
* [姘翠笅鏈哄櫒浜虹墿鐞嗕豢鐪熶笌 6-DOF 閿洏杩愬姩鎺у埗](./water/rov_physical_simulation.md)

* [姘翠笅 ROV 鍏嚜鐢卞害鎵嬫搷涓庢姉娴佽兘鍔涜瘎娴嬩豢鐪焆(./water/rov_handling_eval.md) 鈥斺€?鐢ㄦ紓绉荤巼銆佸悇鍚戝紓鎬ф瘮涓庢搷鎺ф潈闄愬埄鐢ㄧ巼 畏 閲忓寲鎵嬫搷鍝佽川锛岄檮涓夌粍瀵圭収瀹為獙
* [ROV 鎺ㄨ繘鍣ㄩ厤缃煩闃典笌楗卞拰鎰熺煡鎺ㄥ姏鍒嗛厤](./water/rov_thruster_allocation.md) 鈥斺€?8 鎺ㄨ繘鍣?6脳8 閰嶇疆鐭╅樀锛堢З 6銆佹潯浠舵暟 10.9锛夛紝绠辩害鏉?QP 鍒嗛厤锛涜秴鍖呯粶鏃跺姏鏃嬮噺娈嬪樊姣斿厛浼€嗗啀闄愬箙浣?36%锛?0.00 vs 31.41锛?
* [鍔ㄦ€佹磱娴?ROV 閿洏閬ユ搷涓?MLP 宸¤埅鎺у埗](./water/mjc_rov_current_teleop.md)
* [姘翠笅 ROV 澹板憪鍥惧儚 CNN 鐩爣鍒嗙被锛圙azebo 璁粌閾捐矾锛塢(./water/rov_gazebo_sonar_cnn.md) 鈥斺€?Gazebo 閲囬泦鍥惧儚銆? 绫?CNN 璁粌涓?2 Hz 瀹氭椂鎺ㄧ悊锛屾潈閲嶄笌绫诲埆琛ㄩ殢鍖呭畨瑁?
* [鎵嬪啓 PPO 寮哄寲瀛︿範 ROV 杞ㄨ抗璺熻釜涓?PID 鍩虹嚎瀵规瘮](./water/mjc_rov_ppo_tracking.md)

* [鍚屼竴 ROV 浠诲姟 PPO 涓?SAC 寮哄寲瀛︿範绠楁硶瀵规瘮](./water/mjc_rov_rl_compare.md)

### 鍏朵粬锛堢幆澧冦€佹帴鍙ｄ笌瀹瑰櫒锛?
* [姘村煙杞藉叿 ROS2 鎺ュ彛](./water/HoloOcean.md)

* [HoloOcean Windows 鏈満鐜鎼缓](./water/HoloOcean-Windows-Setup.md) 鈥斺€?鍦?Windows 涓婄敤 Conda 瀹夎 Python 瀹㈡埛绔€佷笅杞藉満鏅寘骞惰窇閫氱涓€涓豢鐪?
* [WSL 璺戦€?HoloOcean2 鐨?ROS2 绀轰緥锛堟棤澶存ā寮忥級](./water/WSL_HoloOcean2_ROS2.md) 鈥斺€?鏃?GPU 鐜涓嬬敤 `-nullrhi` 鍙傛暟璺戞棤澶翠豢鐪?
* [Docker 寮€鍙戠幆澧僝(./water/docker.md) 鈥斺€?寮€鍙戝鍣ㄤ笌宸ヤ綔绌洪棿鎸傝浇

* [HoloOcean ROS2 杩愯鏃跺鍣╙(./water/docker_runtime.md) 鈥斺€?鐢?`build_container.sh` 鏋勫缓杩愯鏃堕暅鍍?
* [澹板憪鏁版嵁婊ゆ尝鍒濇楠岃瘉](./water/rov_sonar_filter.md)



濡傛灉瀵规枃妗ｄ腑鐨勪换浣曢棶棰樺彲浠ュ湪 [鏈枃妗ｇ殑婧愮爜浠撳簱](https://github.com/OpenHUTB/ros2) 涓殑 [闂](https://github.com/OpenHUTB/ros2/issues) 椤甸潰璁ㄨ鎴栬€呮彁浜?[鎷夊彇璇锋眰](https://github.com/OpenHUTB/.github/blob/master/CONTRIBUTING.md) 鐩存帴淇敼鏂囨。銆?
___

## 7. 缁忓吀鎺у埗 <span id='classical_control'></span>

* [鍊掔珛鎽嗗钩琛″皬杞?(cart-pole, LQR 鏈€浼樻帶鍒?](./classical_control/cartpole_balance.md) 鈥斺€?鐢?LQR 璁╁€掔珛鎽嗕粠鍊炬枩琚媺鍥炵珫鐩翠繚鎸佷笉鍊?婕旂ず ROS 鍙戝竷/璁㈤槄闂幆涓庢渶浼樻帶鍒?

## 鍙傝€冩枃鐚?* [MuJoCo 澶辫惤鍏洯鏃犱汉鏈虹鍒扮瑙嗚杞悜](./air/mujoco_abandoned_park_uav_visual_steering.md)

# Maintainer: David Runge <dvzrv@archlinux.org>
# Maintainer: Jan Alexander Steffens (heftig) <heftig@archlinux.org>
# Maintainer (Holo): Ludovico de Nittis <denittis@collabora.com>

pkgbase=wireplumber
pkgname=(
  wireplumber
  libwireplumber
)
pkgver=0.5.10
pkgrel=1.11
pkgdesc="Session / policy manager implementation for PipeWire"
url="https://pipewire.pages.freedesktop.org/wireplumber/"
arch=(x86_64)
license=(MIT)
makedepends=(
  doxygen
  gcc-libs
  git
  glib2
  glib2-devel
  glibc
  gobject-introspection
  graphviz
  libpipewire
  lua
  meson
  pipewire
  'python>=3.13'
  'python<3.14'
  python-breathe
  python-lxml
  python-sphinx
  python-sphinx_rtd_theme
  systemd
  systemd-libs
)
checkdepends=(pipewire-audio)
source=(
  "git+https://gitlab.freedesktop.org/pipewire/$pkgbase.git#tag=$pkgver"

  # Holo: backport of https://gitlab.freedesktop.org/pipewire/wireplumber/-/merge_requests/643
  # and https://gitlab.freedesktop.org/pipewire/wireplumber/-/merge_requests/667
  # Part of https://gitlab.steamos.cloud/holo-team/tasks/-/issues/1208
  # and https://gitlab.steamos.cloud/holo-team/tasks/-/issues/564
  "0001-access-default-Allow-defining-object-specific-permis.patch"
  "0002-monitor-alsa-Add-node.create-loopback-property.patch"
  "0003-monitor-alsa-Don-t-make-the-loopback-device-node-vir.patch"
  "0004-monitor-alsa-Dont-set-node-dont-remix-property.patch"
  "0005-monitor-alsa-Add-alsa.loopback-true-to-split-PCM-loo.patch"

  # Holo: backport final patch of https://gitlab.freedesktop.org/pipewire/wireplumber/-/merge_requests/667/commits
  # Addresses https://gitlab.steamos.cloud/holo-team/tasks/-/issues/1340
  "0004-monitor-alsa-Forward-the-session.suspend-timeout-sec.patch"

  # Holo: backport of https://gitlab.freedesktop.org/pipewire/wireplumber/-/merge_requests/719 and
  # https://gitlab.freedesktop.org/pipewire/wireplumber/-/merge_requests/720
  # Fixes https://gitlab.steamos.cloud/holo-team/tasks/-/issues/1729
  "0001-monitor-alsa-increase-priority-for-usb-devices.patch"
  "0001-use-session-and-route-priorities.patch"

  # Holo: backport of https://gitlab.freedesktop.org/pipewire/wireplumber/-/merge_requests/721
  # Addresses https://gitlab.steamos.cloud/holo-team/tasks/-/issues/564
  "0001-m-si-audio-adapter-Configure-the-node-ports-if-the-i.patch"
  "0002-create-item-Reconfigure-audio-adapters-if-node.featu.patch"
  "0003-m-si-audio-adapter-Add-new-item.features.mono-config.patch"
  "0004-config-Add-new-node.features.audio.mono-setting.patch"

  # Holo: backport of https://gitlab.freedesktop.org/pipewire/wireplumber/-/merge_requests/730
  # Fixes https://gitlab.steamos.cloud/holo-team/tasks/-/issues/1754
  "0001-m-lua-scripting-Add-enum_params-Lua-API-for-WpPipewi.patch"
  "0002-state-routes.lua-Make-sure-routes-cache-is-always-up.patch"
  "0003-state-routes-Don-t-save-routes-that-are-not-availabl.patch"
  "0004-apply-routes.lua-Always-set-save-false-when-applying.patch"
  "0005-state-routes.lua-Don-t-save-again-the-route-when-res.patch"

  # Holo: backport of https://gitlab.freedesktop.org/pipewire/wireplumber/-/merge_requests/734
  # Addresses https://gitlab.steamos.cloud/holo-team/tasks/-/issues/588
  "0001-modules-Add-notifications-api-module.patch"
  "0002-scripts-Add-automute-alsa-routes.lua-to-auto-mute-AL.patch"

  # Holo: backport of https://gitlab.freedesktop.org/pipewire/wireplumber/-/merge_requests/737
  # Followup of https://gitlab.steamos.cloud/holo-team/tasks/-/issues/1754
  "0001-state-routes.lua-Make-sure-the-device-is-still-valid.patch"

  # Holo: backport of https://gitlab.freedesktop.org/pipewire/wireplumber/-/merge_requests/749
  "0001-monitor-alsa-Add-a-setting-to-use-HDMI-channel-detec.patch"

  # Holo: backport of https://gitlab.freedesktop.org/pipewire/wireplumber/-/merge_requests/743
  "0001-scripts-Add-node-filter-graph.lua.patch"

  # Holo: backport of https://gitlab.freedesktop.org/pipewire/wireplumber/-/merge_requests/753
  "0001-state-profile-Handle-new-dont-restore-off-profile-rule.patch"

  # Holo: backport of https://gitlab.freedesktop.org/pipewire/wireplumber/-/merge_requests/761
  "0001-monitor-alsa-Also-include-alsa.-device-properties-fo.patch"

  # Holo: backport of https://gitlab.freedesktop.org/pipewire/wireplumber/-/merge_requests/769
  "0001-create-item-Only-configure-audio-device-sink-nodes-i.patch"
)
b2sums=('5c9d06c4084187ce172e98fb05bef3826e4b7bf1fba505e5543fec0e194d8a957172c81e6fa32c7f53832e204dd794189d48deaae5eca10577b04106f2625ff3'
        '86f80f07bb5f446ae90f88f39870139d4d902f99048a62eb825ac12b654ca248568b17f8a1ca15777b41e0a11054345d023fc36a348372f15cb75b92a0180cfe'
        '09ab29570886efb01148edec25a0bb1bcc2ef20e7b02ed6f1fbaa0a29caa4b1f859717735b33fa93ca3494a36336c6730ed940f580ee78705d3c7b6fdc9d5735'
        '145fd614765ebe212de7e27e78b243bb294bd2fdc1efb1c6852280e8db2c2cbca40d6ce838013a06ced34bc030a16a11f1c4875562cd5d041c0785e7be712636'
        '46f72253266c5b9230678946d7b349a5726801d2dd038fa00748e0b5cf194b1d21812862399a95a11f2ae9942a2319304ba2cdd607f6fcacdf382ac5ca57aa01'
        '146bcaf65e9646ff9ce6359920959b15ed4bc5991bb59dca6e2af366d292d621e54feb482e56c3effa4b774d8b5ab857e8ae3bfcf844d0d0b605ba09edc9fd16'
        '3b05b23dd3ff1da4f59df814780cf5251769c10ef3b1c07707ef717160631e27113e5e7286cd8b37ad4f37b21f9f14649d8fa5148b6aa90d26fef48a219e7e5e'
        'd8e0ff4f2c0927e1da127442c2c3d9aecaa05cca2753fdcb1786fe2ac6d959b0a995988e02f155de396fbe4fcb5eac3cbd55caa75be6d4a86eaa3e723415d062'
        'aba4d3fd93a4dafac5c1bb425621b176a80b3396f2896102c0c26399e86d9101165dabd0dee2c9d8964415e5098a8b78e87b564d2855de6c81f3eca489b183da'
        '40a604ee6b0b2e1f36fbbeacfcc6ef937d660d48aaab7ec307efbfbd3ad14ad6c869f46c08b81de383ec31f6cc870bd432cd2a1a3c41437d2281427a66c14541'
        'be0fd13aadbad2f2135a7a84197ae1d73a3eaf1da89dc856e032a1ddc1ff666548f69adf5e89f15e80ad29b57888d76b90a99a7a7897ff387f9e6ef65369d8ba'
        'b0ee137c10d676ac6ee33bf1431467b0e5b278bf798581a51449572db2eec5668cde787e7ec81ac1f9a2fc6e7cc2d60158daf8fcafceb3a3cff999f858f63b1a'
        'a16666f32605b1e52d586b613033a0428d8b018a8c15941a9e5404866307a4ed69fc3748a5fd7490f83f2782d40c7b920f16c7286070c9da3e6c28ff945a0101'
        '98ec78af076462b5857b6b43fad5ff8966dbafab484ea4d6cd5fc9a7d7408426ff3bedd485288ccecde8a661775c1d17e27ca35ac77eee1aaa5cf53ab59ffa40'
        'd5c8796bd477e19847ea004accaab08ea96f22ac1eeb0e2a50d905385a2947171c1921fd73efc21cbbc18e81588fab258feda549ebd1568859bb710a4e83637e'
        '5e498f32efd015115a9e983475f26ea61a70b8f5fa7a93509ba5a5ba50bbc04ab5f39c2fe18b24969bffb683ba2a561732cb0256e42de323cd6b301123e535d4'
        '8beef92428552a4f17e70459a1669352c93ce4b8a1fd85ac2fc6e6ee7c9a886c2f64e87e7bf2e9e6029a168ad9af17b1faa9249e001afcaeac5a2c32b52dcbdc'
        '19be7fa178a06365ffb9094e37130f51e2e8aae8027f080b8c36fd135b97f7c7ebc1e2cd32585c025b21b31127059f94aa70c93ee48b8d27c74119f4c7b38504'
        '683282b840c6257e36b24fa4125dc68a4af152451b466621b2eadd959ac2c177caa7fead9494b2131744a596d1c3fd88aaffe99bb1608c1ea3e07b5dfa4f2d7c'
        'bb310edffbd7b041119344ff82a33562c472a70a76ed33c4121c8cb178df9403036c176c50a8ec58134191a434bbf34a3e560ab83272910a72a10a8e6aa689c8'
        '4d9c5e2e605a37cd670e8248e4f8e5dd244a755337c38527a1959f5ef301466d5d062ed86a334ea673c397d53e0a9dc3a98f2be29cb3faf00fc2e1245dae0929'
        'e1b5b58500c2dfb52d8d6a30d55ad485775025b446523edfa42ea96fa8608a26cbdeb894b02128c7098d0833a98ef8c5937c7f478ce267769a61dacf4f501ab8'
        '55d54fb9527ab9d7d70eb72abfd337209cdcd88732133a75b14565acc942c7c85d9833e1b577dc387a1cc55f3a89ebe0d8e04bb1ea6acc0509253bb0db5b4512'
        'ab233036f723a290d1b72258402550483b68dbc181784c06bf3c1c815fb8c9a7a3ba89ea9e2d44fa68bf2c5199fd1e4fe4a5e447ba830767514d1587b4a25190'
        'fa814c004a0cb671da80bfecf20bc6d849f6ddd36cd550e6a2781e0592370ebd44516d6740b4a60814b636e15823edcef2db399598a9d2efe8d5056bb17e575e'
        'ada0dd84022808651653bf1fa61c15175bf51157f140f42c0ba854ee578dba4b10ed668a2471013669cc101d67bd3b1864c2693262b5b850dfc72940cce02c0d')

prepare() {
  cd $pkgbase

  # Holo: apply downstream patches
  local src
  for src in "${source[@]}"; do
    [[ $src = *.patch ]] || continue
    src="${src##*/}"
    echo "Applying patch $src..."
    patch -Np1 < "../$src"
  done
}

build() {
  local meson_options=(
    -D elogind=disabled
    -D system-lua=true
    -D doc=disabled # HOLO: Fails due to some locale gubbins -- disable.
  )

  arch-meson $pkgbase build "${meson_options[@]}"
  meson compile -C build
}

check() {
  meson test -C build --print-errorlogs
}

_pick() {
  local p="$1" f d; shift
  for f; do
    d="$srcdir/$p/${f#$pkgdir/}"
    mkdir -p "$(dirname "$d")"
    mv "$f" "$d"
    rmdir -p --ignore-fail-on-non-empty "$(dirname "$f")"
  done
}

_ver=${pkgver:0:3}

package_wireplumber() {
  depends=(
    "libwireplumber=$pkgver-$pkgrel"
    gcc-libs
    glibc
    libg{lib,object,io}-2.0.so
    libpipewire
    libpipewire-0.3.so
    libsystemd.so
    lua
    pipewire
    systemd-libs
  )
  optdepends=(
    'wireplumber-docs: Documentation'
  )
  provides=(pipewire-session-manager)
  conflicts=(pipewire-media-session)
  install=wireplumber.install

  meson install -C build --destdir "$pkgdir"

  (
    cd "$pkgdir"

    _pick libw usr/lib/libwireplumber-$_ver.so*
    _pick libw usr/lib/girepository-1.0
    _pick libw usr/lib/pkgconfig
    _pick libw usr/include
    _pick libw usr/share/gir-1.0

    _pick docs usr/share/doc
  )

  install -Dt "$pkgdir/usr/share/doc/$pkgname" -m644 $pkgbase/{NEWS,README}*
  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 $pkgbase/LICENSE
}

package_libwireplumber() {
  pkgdesc+=" - client library"
  depends=(
    gcc-libs
    glibc
    libg{lib,module,object,io}-2.0.so
    libpipewire-0.3.so
  )
  provides=(libwireplumber-$_ver.so)

  mv libw/* "$pkgdir"

  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 $pkgbase/LICENSE
}

# vim:set sw=2 et:

# Maintainer: David Runge <dvzrv@archlinux.org>
# Maintainer: Jan Alexander Steffens (heftig) <heftig@archlinux.org>
# Contributor: Jan de Groot <jgc@archlinux.org>

pkgbase=pipewire
pkgname=(
  pipewire
  libpipewire
  alsa-card-profiles
  pipewire-docs
  pipewire-audio
  pipewire-alsa
  pipewire-jack
  pipewire-pulse
  gst-plugin-pipewire
  pipewire-zeroconf
  pipewire-v4l2
  pipewire-x11-bell
  pipewire-session-manager
  pulse-native-provider
)
_commit=6ab86209f23a841de7eac6bc0c1009aceb9ffd87  # tags/1.0.3
pkgver=1.0.3
_so_ver=0.3
pkgrel=1
epoch=1
pkgdesc="Low-latency audio/video router and processor"
url="https://pipewire.org"
arch=(x86_64)
license=(MIT)
makedepends=(
  alsa-lib
  avahi
  bluez-libs
  dbus
  doxygen
  git
  glib2
  graphviz
  gst-plugins-base
  libcanberra
  libfdk-aac
  libfreeaptx
  liblc3
  libldac
  libmysofa
  libpulse
  libsndfile
  libusb
  libx11
  libxfixes
  lilv
  meson
  ncurses
  opus
  python-docutils
  readline
  rtkit
  sbc
  sdl2
  systemd
  valgrind
  webrtc-audio-processing-1
)
checkdepends=(
  desktop-file-utils
  openal
)
options=(debug)
source=(
    "git+https://gitlab.freedesktop.org/pipewire/pipewire.git#commit=$_commit"
)

sha256sums=(
    'SKIP'
)

pkgver() {
  cd pipewire
  git describe --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  cd pipewire

  # Holo: apply downstream patches
  local src
  for src in "${source[@]}"; do
    [[ $src = *.patch ]] || continue
    src="${src##*/}"
    echo "Applying patch $src..."
    patch -Np1 < "../$src"
  done

  # remove export of LD_LIBRARY_PATH for pw-jack as it would add /usr/lib
  sed -i '/LD_LIBRARY_PATH/d' pipewire-jack/src/pw-jack.in
}

build() {
  # Holo: our build is lacking libcamera support
  local meson_options=(
    -D bluez5-codec-lc3plus=disabled
    -D docs=enabled
    -D jack-devel=true
    -D jack=disabled
    -D libffado=disabled
    -D libcamera=disabled
    -D libjack-path=/usr/lib
    -D man=enabled
    -D roc=disabled
    -D rlimits-install=false
    -D selinux=disabled
    -D session-managers=[]
    -D udevrulesdir=/usr/lib/udev/rules.d
  )

  arch-meson pipewire build "${meson_options[@]}"
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

package_pipewire() {
  license+=(LGPL-2.1-or-later)  # libspa-alsa
  depends=(
    gcc-libs
    glibc
    "libpipewire=$epoch:$pkgver-$pkgrel"
    libdbus-1.so
    libglib-2.0.so
    libncursesw.so
    libpipewire-$_so_ver.so
    libreadline.so
    libsystemd.so
    libudev.so
  )
  optdepends=(
    'gst-plugin-pipewire: GStreamer plugin'
    'pipewire-alsa: ALSA configuration'
    'pipewire-audio: Audio support'
    'pipewire-docs: Documentation'
    'pipewire-jack: JACK replacement'
    'pipewire-pulse: PulseAudio replacement'
    'pipewire-session-manager: Session manager'
    'pipewire-v4l2: V4L2 interceptor'
    'pipewire-x11-bell: X11 bell'
    'pipewire-zeroconf: Zeroconf support'
    'realtime-privileges: realtime privileges with rt module'
    'rtkit: realtime privileges with rtkit module'
  )
  install=pipewire.install

  meson install -C build --destdir "$pkgdir"

  (
    cd "$pkgdir"

    # Replace copies with symlinks
    for _f in pipewire-{aes67,avb,pulse}; do
      cmp usr/bin/pipewire usr/bin/$_f
      ln -sf pipewire usr/bin/$_f
    done

    _pick lib usr/include/{pipewire-$_so_ver,spa-0.2}
    _pick lib usr/lib/libpipewire-$_so_ver.so*
    _pick lib usr/lib/pkgconfig/lib{pipewire-$_so_ver,spa-0.2}.pc

    _pick acp usr/lib/udev
    _pick acp usr/share/alsa-card-profile

    _pick docs usr/share/doc

    _pick audio usr/bin/pipewire-{aes67,avb}
    _pick audio usr/bin/pw-{cat,{,enc}play,record,midi{play,record},dsdplay}
    _pick audio usr/bin/pw-{loopback,mididump}
    _pick audio usr/bin/spa-{acp-tool,resample}
    _pick audio usr/lib/alsa-lib
    _pick audio usr/lib/pipewire-$_so_ver/libpipewire-module-avb.so
    _pick audio usr/lib/pipewire-$_so_ver/libpipewire-module-echo-cancel.so
    _pick audio usr/lib/pipewire-$_so_ver/libpipewire-module-fallback-sink.so
    _pick audio usr/lib/pipewire-$_so_ver/libpipewire-module-filter-chain*.so
    _pick audio usr/lib/pipewire-$_so_ver/libpipewire-module-loopback.so
    _pick audio usr/lib/pipewire-$_so_ver/libpipewire-module-netjack2-*.so
    _pick audio usr/lib/pipewire-$_so_ver/libpipewire-module-pipe-tunnel.so
    _pick audio usr/lib/pipewire-$_so_ver/libpipewire-module-protocol-simple.so
    _pick audio usr/lib/pipewire-$_so_ver/libpipewire-module-rtp-{sap,sink,source}.so
    _pick audio usr/lib/pipewire-$_so_ver/libpipewire-module-vban-{recv,send}.so
    _pick audio usr/lib/spa-0.2/{aec,alsa,audio*,avb,bluez5}
    _pick audio usr/lib/systemd/user/filter-chain.service
    _pick audio usr/share/alsa
    _pick audio usr/share/man/man1/pw-{cat,loopback,mididump}.1
    _pick audio usr/share/man/man7/libpipewire-module-{avb,echo-cancel,fallback-sink,filter-chain*,loopback,netjack2*,pipe-tunnel,protocol-simple,rtp-{sap,sink,source},vban*}.7
    _pick audio usr/share/pipewire/filter-chain*
    _pick audio usr/share/pipewire/pipewire-{aes67,avb}.conf
    _pick audio usr/share/spa-0.2/bluez5

    _pick jack usr/bin/pw-jack
    _pick jack usr/include/jack
    _pick jack usr/lib/libjack*
    _pick jack usr/lib/pkgconfig/jack.pc
    _pick jack usr/share/man/man1/pw-jack.1
    _pick jack usr/share/pipewire/jack.conf

    _pick pulse usr/bin/pipewire-pulse
    _pick pulse usr/lib/pipewire-$_so_ver/libpipewire-module-protocol-pulse.so
    _pick pulse usr/lib/pipewire-$_so_ver/libpipewire-module-pulse-tunnel.so
    _pick pulse usr/lib/systemd/user/pipewire-pulse.*
    _pick pulse usr/share/man/man1/pipewire-pulse.1
    _pick pulse usr/share/man/man5/pipewire-pulse.conf.5
    _pick pulse usr/share/man/man7/pipewire-pulse*.7
    _pick pulse usr/share/man/man7/libpipewire-module-{protocol-pulse,pulse-tunnel}.7
    _pick pulse usr/share/pipewire/pipewire-pulse.conf

    _pick gst usr/lib/gstreamer-1.0

    _pick zeroconf usr/lib/pipewire-$_so_ver/libpipewire-module-{raop,zeroconf}-*.so
    _pick zeroconf usr/lib/pipewire-$_so_ver/libpipewire-module-rtp-session.so
    _pick zeroconf usr/share/man/man7/libpipewire-module-{raop-*,rtp-session,zeroconf*}.7

    _pick v4l2 usr/bin/pw-v4l2 usr/lib/pipewire-$_so_ver/v4l2

    _pick x11-bell usr/lib/pipewire-$_so_ver/libpipewire-module-x11-bell.so
    _pick x11-bell usr/share/man/man7/libpipewire-module-x11-bell.7

    # directories for overrides
    mkdir -p etc/pipewire
    for _l in {client-rt,client,minimal,pipewire}.conf.d
    do
      ln -s /run/pipewire/${_l} etc/pipewire/${_l}
    done
  )

  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 pipewire/COPYING
}

package_libpipewire() {
    pkgdesc+=" - client library"
  depends=(
    glibc
    gcc-libs
  )
  provides=(libpipewire-$_so_ver.so)

  mv lib/* "$pkgdir"

  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 pipewire/COPYING
}

package_alsa-card-profiles() {
  pkgdesc+=" - ALSA card profiles"
  license=(LGPL-2.1-or-later)

  mv acp/* "$pkgdir"
}

package_pipewire-docs() {
  pkgdesc+=" - documentation"

  mv docs/* "$pkgdir"

  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 pipewire/COPYING
}

package_pipewire-audio() {
  pkgdesc+=" - Audio support"
  depends=(
    alsa-card-profiles
    dbus
    gcc-libs
    glib2
    glibc
    libasound.so
    libbluetooth.so
    libfdk-aac.so
    libfreeaptx.so
    liblc3.so
    libldacBT_enc.so
    liblilv-0.so
    libmysofa.so
    libopus.so
    libpipewire-$_so_ver.so
    libsbc.so
    libsndfile.so
    libusb-1.0.so
    libwebrtc-audio-processing-1.so
    pipewire
    systemd-libs
  )

  mv audio/* "$pkgdir"

  mkdir -p "$pkgdir/etc/alsa/conf.d"
  ln -st "$pkgdir/etc/alsa/conf.d" \
    /usr/share/alsa/alsa.conf.d/50-pipewire.conf

  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 pipewire/COPYING
}

package_pipewire-alsa() {
  pkgdesc+=" - ALSA configuration"
  depends=(
    pipewire
    pipewire-audio
    pipewire-session-manager
  )
  conflicts=(pulseaudio-alsa)
  provides=(pulseaudio-alsa)

  mkdir -p "$pkgdir/etc/alsa/conf.d"
  ln -st "$pkgdir/etc/alsa/conf.d" \
    /usr/share/alsa/alsa.conf.d/99-pipewire-default.conf

  install -Dm644 /dev/null \
    "$pkgdir/usr/share/pipewire/media-session.d/with-alsa"

  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 pipewire/COPYING
}

package_pipewire-jack() {
  pkgdesc+=" - JACK replacement"
  license+=(LGPL-2.1-or-later GPL-2.0-only)  # libjackserver
  depends=(
    glibc
    libpipewire-$_so_ver.so
    pipewire
    pipewire-audio
    pipewire-session-manager
    sh
  )
  optdepends=('jack-example-tools: for official JACK example-clients and tools')
  conflicts=(jack jack2 pipewire-jack-client)
  provides=(jack libjack.so libjackserver.so libjacknet.so)

  mv jack/* "$pkgdir"

  install -Dm644 /dev/null \
    "$pkgdir/usr/share/pipewire/media-session.d/with-jack"

  # directories for overrides
  mkdir -p "$pkgdir"/etc/pipewire
  ln -s /run/pipewire/jack.conf.d "$pkgdir"/etc/pipewire/jack.conf.d

  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 pipewire/COPYING
}

package_pipewire-pulse() {
  pkgdesc+=" - PulseAudio replacement"
  depends=(
    dbus
    gcc-libs
    glibc
    libavahi-{client,common}.so
    libglib-2.0.so
    libpipewire-$_so_ver.so
    libpulse.so
    pipewire
    pipewire-audio
    pipewire-session-manager
    systemd-libs
  )
  provides=(
    pulse-native-provider
    pulseaudio
    pulseaudio-bluetooth
  )
  conflicts=(
    pulseaudio
    pulseaudio-bluetooth
  )
  install=pipewire-pulse.install

  mv pulse/* "$pkgdir"

  # directory for overrides
  mkdir -p "$pkgdir"/etc/pipewire
  ln -s /run/pipewire/pipewire-pulse.conf.d \
     "$pkgdir"/etc/pipewire/pipewire-pulse.conf.d

  install -Dm644 /dev/null \
    "$pkgdir/usr/share/pipewire/media-session.d/with-pulseaudio"

  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 pipewire/COPYING
}

package_gst-plugin-pipewire() {
  pkgdesc="Multimedia graph framework - pipewire plugin"
  depends=(
    glib2
    glibc
    gst-plugins-base-libs
    gstreamer
    libpipewire-$_so_ver.so
    pipewire
    pipewire-session-manager
  )

  mv gst/* "$pkgdir"

  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 pipewire/COPYING
}

package_pipewire-zeroconf() {
  pkgdesc+=" - Zeroconf support"
  depends=(
    gcc-libs
    glibc
    libavahi-{client,common}.so
    libpipewire-$_so_ver.so
    openssl
    opus
    pipewire
    pipewire-audio
  )

  mv zeroconf/* "$pkgdir"

  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 pipewire/COPYING
}

package_pipewire-v4l2() {
  pkgdesc+=" - V4L2 interceptor"
  depends=(
    glibc
    libpipewire-$_so_ver.so
    pipewire
    pipewire-session-manager
    sh
  )

  mv v4l2/* "$pkgdir"

  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 pipewire/COPYING
}

package_pipewire-x11-bell() {
  pkgdesc+=" - X11 bell"
  depends=(
    glibc
    libcanberra.so
    libpipewire-$_so_ver.so
    libx11
    libxfixes
    pipewire
    pipewire-audio
  )

  mv x11-bell/* "$pkgdir"

  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 pipewire/COPYING
}

package_pipewire-session-manager() {
  pkgdesc="Session manager for PipeWire (default provider)"
  depends=(wireplumber)
}

package_pulse-native-provider() {
  pkgdesc="PulseAudio sound server (default provider)"
  depends=(pipewire-pulse)
}

# vim:set sw=2 sts=-1 et:

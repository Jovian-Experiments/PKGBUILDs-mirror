# Maintainer: Umang Jain (uajain) <uajain@igalia.com>

pkgbase=linux-neptune-73-devel
_tag=7.3.1-valve1
pkgver=${_tag//-/.}
pkgrel=1
pkgdesc='Linux'
url="https://gitlab.steamos.cloud/jupiter/linux-integration/-/tree/$_tag"
arch=(
  x86_64
)
license=(GPL-2.0-only)
makedepends=(
  bc
  binutils
  cpio
  gettext
  glibc
  libelf
  libgcc
  openssl
  pahole
  perl
  python
  rust
  rust-bindgen
  rust-src
  tar
  xxhash
  xz
  zlib
  zstd

  # Jupiter: we don't build docs, we don't need it's deps
  # # htmldocs
  # graphviz
  # imagemagick
  # python-sphinx
  # python-yaml
  # texlive-latexextra

  # Jupiter: we're using git+ssh for the source
  git
  openssh
)
options=(
  !debug
  !strip
)
_srcname=archlinux-linux-neptune-devel
source=(
  "$_srcname::git+ssh://git@gitlab.steamos.cloud/jupiter/linux-integration.git#tag=$_tag"
  config-neptune  # Jupiter: the neptune kernel fragment file (overrides 'config.x86_64')
  config-neptune-devel  # Jupiter: the neptune devel kernel fragment file
)
source_x86_64=(config.x86_64)
validpgpkeys=(
  ABAF11C65A2970B130ABE3C479BE3E4300411886  # Linus Torvalds
  647F28654894E3BD457199BE38DBBDC86092693E  # Greg Kroah-Hartman
  83BC8889351B5DEBBB68416EB8AC08600F108CDF  # Jan Alexander Steffens (heftig)
)
sha256sums=('6da0e666f50c35f2b40f4037c43801ef9f53c8b42c100b5813adc0cd51905d56'
            'b91c3ed65067704c8fdb8289d44ed18aa62f98f52c3b6d91fb72bc5b1606ae79'
            'a9e0f3aa421a4cd2ccc840853d52b7aaeb2e2792238e4e953d0776f0f3061bc6')
sha256sums_x86_64=('ecd8c76eb203493e67ba4052e7bc1fa46f51c91566f102172e7a18d7de2dd5eb')
b2sums=('eae29412fff6b06990c4c9b082b859054cc98f6cb10b361ff3399ef474fcf9944e0e7386d38aaaeb41e82fb367160023e3c1128ee915c83a4419605036bf35e8'
        'c5bbcc97d48ed12574e8491211e4cfbadcf5f9e696c6c046e5f87f84550c2491950d1be0eca83cff6e35f74a0350d1cd2f8627e5fcd70d93bfc25ca96b4eddd1'
        'eda0ef94f42e722d14cbfe814bada22a1b3aec02a587aebe949290e4ee77286e66298cb62dff7fbf603f4366a4e8bc11eba932ef51074c64e037605775feb91d')
b2sums_x86_64=('0564ea851810a155cd589bd3a5d74344f16ab2c7c5ea5aa740faaf6776230ccd115474b6164ebd32d89d8615e41d24d2612d649b987f1f2cde58476e5561fe5e')

# https://www.kernel.org/pub/linux/kernel/v7.x/sha256sums.asc

export KBUILD_BUILD_HOST=archlinux
export KBUILD_BUILD_USER=$pkgbase
export KBUILD_BUILD_TIMESTAMP="$(date -Ru${SOURCE_DATE_EPOCH:+d @$SOURCE_DATE_EPOCH})"

prepare() {
  cd $_srcname

  echo "Setting version..."
  echo "-$pkgrel" > localversion.10-pkgrel
  echo "${pkgbase#linux}" > localversion.20-pkgname

  local src
  for src in "${source[@]}"; do
    src="${src%%::*}"
    src="${src##*/}"
    src="${src%.zst}"
    [[ $src = *.patch ]] || continue
    echo "Applying patch $src..."
    patch -Np1 < "../$src"
  done

  echo "Setting config..."
  cp ../config.$CARCH .config
  scripts/kconfig/merge_config.sh -m ../config.$CARCH ../config-neptune ../config-neptune-devel
  make olddefconfig
  diff -u ../config.$CARCH .config || :

  make -s kernelrelease > version
  echo "Prepared $pkgbase version $(<version)"
}

build() {
  cd $_srcname
  # Jupiter: Don't build the docs
  # make htmldocs SPHINXOPTS=-QT &
  # local pid_docs=$!

  make all
  make -C tools/bpf/bpftool vmlinux.h feature-clang-bpf-co-re=1
  # wait $pid_docs
}

_package() {
  pkgdesc="The $pkgdesc kernel and modules"
  depends=(
    coreutils
    initramfs
    kmod
  )
  optdepends=(
    'linux-firmware: firmware images needed for some devices'
    'scx-scheds: to use sched-ext schedulers'
    'wireless-regdb: to set the correct wireless channels of your country'
  )
  provides=(
    KSMBD-MODULE
    VIRTUALBOX-GUEST-MODULES
    WIREGUARD-MODULE
  )
  replaces=(
    virtualbox-guest-modules-arch
    wireguard-arch
  )

  cd $_srcname
  local modulesdir="$pkgdir/usr/lib/modules/$(<version)"

  echo "Installing boot image..."
  # systemd expects to find the kernel here to allow hibernation
  # https://github.com/systemd/systemd/commit/edda44605f06a41fb86b7ab8128dcf99161d2344
  install -Dm644 "$(make -s image_name)" "$modulesdir/vmlinuz"

  # Used by mkinitcpio to name the kernel
  echo "$pkgbase" | install -Dm644 /dev/stdin "$modulesdir/pkgbase"

  echo "Installing modules..."
  ZSTD_CLEVEL=19 make INSTALL_MOD_PATH="$pkgdir/usr" INSTALL_MOD_STRIP=1 \
    DEPMOD=/doesnt/exist modules_install  # Suppress depmod

  # remove build link
  rm "$modulesdir"/build
}

pkgname=(
  "$pkgbase"
)
for _p in "${pkgname[@]}"; do
  eval "package_$_p() {
    $(declare -f "_package${_p#$pkgbase}")
    _package${_p#$pkgbase}
  }"
done

# vim:set ts=8 sts=2 sw=2 et:

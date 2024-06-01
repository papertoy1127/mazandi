TIERS = (
    "Unrated",
    "Bronze 5", "Bronze 4", "Bronze 3", "Bronze 2", "Bronze 1",
    "Silver 5", "Silver 4", "Silver 3", "Silver 2", "Silver 1",
    "Gold 5", "Gold 4", "Gold 3", "Gold 2", "Gold 1",
    "Platinum 5", "Platinum 4", "Platinum 3", "Platinum 2", "Platinum 1",
    "Diamond 5", "Diamond 4", "Diamond 3", "Diamond 2", "Diamond 1",
    "Ruby 5", "Ruby 4", "Ruby 3", "Ruby 2", "Ruby 1",
    "Master"
)

THEMES = {
  # THEME: {TIER: [background-color, color1, color2, color3, color4, text-color], ...}
  'LIGHT': {
    'border': '#bfbfbf',
    'background': '#f7f8f9',
    'Unknown': ['#dddfe0', '#666666', '#000000', '#000000', '#000000', '#000000'],
    'Unrated': ['#666666', '#424242', '#040202', '#040202', '#040202', '#040202'],
    'Bronze': ['#F1F0F5', '#bd7733', '#B5987B', '#8E6C51', '#5D432F', '#A25B36'],
    'Silver': ['#F1F0F5', '#687f94', '#A1A5B2', '#7B7B9A', '#585865', '#5F606A'],
    'Gold': ['#F5F3F0', '#efae33', '#FFE765', '#FFC455', '#FF961D', '#FDC456'],
    'Platinum': ['#F0F5F3', '#52e7b6', '#8CF8BF', '#39EACF', '#06CBE5', '#39E09D'],
    'Diamond': ['#F1F0F5', '#33c3fc', '#A5F7F7', '#32DDF4', '#157DE5', '#1AC0F2'],
    'Ruby': ['#F5F3F0', '#f7337b', '#FDB8DE', '#F27399', '#E51062', '#DB306B'],
    'Master': ['#F3F0F5', '#CCFFFD', '#D5CBFF', '#E882F5', '#FC62B5', '#CB7CEF'],
  },
  'DARK': {
    'border': '#5c5c5c',
    'background': '#0b131b',
    'Unknown': ['#15202b', '#2f2f2f', '#2f2f2f', '#2f2f2f', '#2f2f2f', '#afafaf'],
    'Unrated': ['#3a3a3a', '#424242', '#1f1f1f', '#0f0f0f', '#0f0f0f', '#dddddd'],
    'Bronze': ['#48423c', '#bd7733', '#a16b36', '#B18151', '#E6AD73', '#bb7027'],
    'Silver': ['#494b4c', '#687f94', '#969899', '#ccd1d3', '#F8FDFF', '#94989b'],
    'Gold': ['#584c3d', '#efae33', '#896512', '#E69A42', '#FCCB6F', '#FDC456'],
    'Platinum': ['#475C55', '#52e7b6', '#2FA57E', '#39E09D', '#00FFE2', '#39E09D'],
    'Diamond': ['#515055', '#33c3fc', '#5489a3', '#57bcec', '#98DEFF', '#1AC0F2'],
    'Ruby': ['#64464e', '#f7337b', '#A22B4E', '#E06087', '#FFA7C2', '#f5457b'],
    'Master': ['#504E58', '#546C71', '#926D9D', '#C970BB', '#FF7CA8', '#CB7CEF'],
  }
}

TIER_RATES = (
    0, # unranked
    30, 60, 90, 120, 150, # bronze
    200, 300, 400, 500, 650, # silver
    800, 950, 1100, 1250, 1400, # gold
    1600, 1750, 1900, 2000, 2100, # platinum
    2200, 2300, 2400, 2500, 2600, # diamond
    2700, 2800, 2850, 2900, 2950, # ruby
    3000 # master
)
